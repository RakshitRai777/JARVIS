from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List

from ai.embeddings.chunk import Chunk
from ai.embeddings.hybrid_ranker import HybridRanker
from ai.web.ranking.cross_encoder_ranker import CrossEncoderRanker
from ai.web.cache.web_cache import WebCache
from ai.web.intent.intent_classifier import IntentClassifier
from ai.web.retrieval.retrieval_policy import RetrievalPolicy
from ai.web.chunking.semantic_chunker import SemanticChunker
from ai.web.scraper.content_cleaner import ContentCleaner
from ai.web.scraper.html_parser import HtmlParser
from ai.web.scraper.page_downloader import PageDownloader
from ai.web.search.search_manager import SearchManager
from ai.web.ranking.bm25_prefilter import BM25PreFilter
from ai.web.ranking.source_diversity import SourceDiversity


class WebPipeline:
    """
    Production Web Retrieval Pipeline

    Pipeline
    --------
    Search
        ↓
    Parallel Page Processing
        ↓
    Cache Lookup
        ↓
    Download
        ↓
    Parse
        ↓
    Clean
        ↓
    Chunk
        ↓
    Save Cache
        ↓
    Hybrid Ranking
        ↓
    Source Diversity
        ↓
    Return Best Chunks
    """

    ############################################################

    MAX_CHUNKS_PER_SOURCE = 2
    MIN_WORDS_PER_CHUNK = 40

    ############################################################

    def __init__(self):

        self.search = SearchManager()

        self.downloader = PageDownloader()

        self.parser = HtmlParser()

        self.cleaner = ContentCleaner()

        self.chunker = SemanticChunker()

        self.prefilter = BM25PreFilter()

        self.ranker = HybridRanker()

        self.cross_ranker = CrossEncoderRanker()

        self.source_diversity = SourceDiversity()

        self.cache = WebCache()

        self.intent_classifier = IntentClassifier()

        self.retrieval_policy = RetrievalPolicy()

    ############################################################

    def _process_page(
        self,
        result,
        config,
    ) -> List[Chunk]:

        if not result.url:
            return []

        if not result.url.startswith(("http://", "https://")):
            return []

        try:

            print(f"[WebPipeline] Processing {result.url}")

            ####################################################
            # Cache
            ####################################################

            cache_entry = self.cache.load(result.url)

            if cache_entry is not None:

                chunks = cache_entry.chunks

                for chunk in chunks:

                    chunk.title = result.title

                    chunk.source = result.url

                print(
                    f"[WebPipeline] Cache returned "
                    f"{len(chunks)} chunks."
                )

                return chunks

            ####################################################
            # Download
            ####################################################

            html = self.downloader.download(result.url)

            if not html:

                print("[WebPipeline] Empty HTML.")

                return []

            ####################################################
            # Parse
            ####################################################

            parsed = self.parser.parse(html)

            if not parsed.strip():

                print("[WebPipeline] Empty parsed content.")

                return []

            ####################################################
            # Clean
            ####################################################

            cleaned = self.cleaner.clean(parsed)

            ####################################################
            # Chunk
            ####################################################

            chunks = self.chunker.chunk(cleaned)

            ####################################################
            # Remove low-quality chunks
            ####################################################

            filtered = []

            for chunk in chunks:

                words = len(chunk.text.split())

                if words < self.MIN_WORDS_PER_CHUNK:
                    continue

                filtered.append(chunk)

            chunks = filtered

            print(
                f"[WebPipeline] "
                f"Filtered to {len(chunks)} useful chunks."
            )

            ####################################################
            # Metadata
            ####################################################

            for chunk in chunks:

                chunk.title = result.title

                chunk.source = result.url

            ####################################################
            # Cache
            ####################################################

            self.cache.save(

                url=result.url,

                title=result.title,

                chunks=chunks,

            )

            print(
                f"[WebPipeline] Created "
                f"{len(chunks)} chunks."
            )

            return chunks

        except Exception as e:

            print(f"[WebPipeline] Failed: {result.url}")

            print(e)

            return []

    ############################################################

    def retrieve(
        self,
        question: str,
    ) -> List[Chunk]:

        print(f"[WebPipeline] Searching: {question}")

        ########################################################
        # Adaptive Retrieval Policy
        ########################################################

        intent = self.intent_classifier.classify(question)

        config = self.retrieval_policy.get(intent)

        print()

        print(
            f"[RetrievalPolicy] "
            f"Intent={intent.value} | "
            f"Pages={config.max_pages} | "
            f"Chunks/Page={config.max_chunks_per_page} | "
            f"Final Chunks={config.top_chunks}"
        )

        ########################################################
        # Search
        ########################################################

        search_results = self.search.search(question)

        if not search_results:

            print("[WebPipeline] No search results.")

            return []

        ########################################################
        # Parallel Processing
        ########################################################

        all_chunks = []

        successful_sources = 0

        max_workers = min(
            config.max_pages,
            len(search_results),
        )

        with ThreadPoolExecutor(
            max_workers=max_workers
        ) as executor:

            futures = {

                executor.submit(
                    self._process_page,
                    result,
                    config,
                ): result

                for result in search_results[:config.max_pages]

            }

            for future in as_completed(futures):

                try:

                    chunks = future.result()

                except Exception as e:

                    print(e)

                    continue

                if not chunks:
                    continue

                all_chunks.extend(chunks)

                successful_sources += 1

                if successful_sources >= config.max_pages:
                    break

        ########################################################

        if not all_chunks:

            print("[WebPipeline] No chunks collected.")

            return []

        ########################################################
        # BM25 Pre-filter
        ########################################################

        prefiltered = self.prefilter.filter(
            question=question,
            chunks=all_chunks,
            top_k=30,
        )

        ########################################################
        # Hybrid Ranking
        ########################################################

        ranked = self.ranker.rank(

            question=question,

            chunks=prefiltered,

            top_results=len(prefiltered),

        )

        ########################################################
        # Per-page limit
        ########################################################

        limited = []

        page_counter = defaultdict(int)

        for chunk in ranked:

            if page_counter[chunk.source] >= config.max_chunks_per_page:
                continue

            limited.append(chunk)

            page_counter[chunk.source] += 1

        ########################################################
        # Source Diversity
        ########################################################

        final_chunks = self.source_diversity.diversify(
            chunks=limited,
            max_per_source=1,
            top_k=config.top_chunks,
        )

        ########################################################
        # Cross Encoder Re-ranking
        ########################################################

        final_chunks = self.cross_ranker.rerank(
            question=question,
            chunks=final_chunks,
            top_k=config.top_chunks,
        )

        print(
            f"[WebPipeline] Returning "
            f"{len(final_chunks)} ranked chunks."
        )

        return final_chunks