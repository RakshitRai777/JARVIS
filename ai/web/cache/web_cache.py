import hashlib
import pickle
from pathlib import Path
from typing import Optional

from ai.web.cache.cache_entry import CacheEntry


class WebCache:
    """
    Disk-based cache for processed webpages.

    Features
    --------
    • Persistent cache
    • Version checking
    • Automatic invalidation
    • Corruption recovery
    • Last-access updates
    """

    ############################################################

    CACHE_VERSION = 2

    CACHE_DIR = Path("data/cache/web")

    ############################################################

    def __init__(self):

        self.CACHE_DIR.mkdir(

            parents=True,

            exist_ok=True

        )

    ############################################################

    def _filename(

        self,

        url: str

    ) -> Path:

        digest = hashlib.sha256(

            url.encode("utf-8")

        ).hexdigest()

        return self.CACHE_DIR / f"{digest}.pkl"

    ############################################################

    def load(

        self,

        url: str

    ) -> Optional[CacheEntry]:

        path = self._filename(url)

        if not path.exists():

            print("[WebCache] MISS")

            return None

        try:

            with open(path, "rb") as file:

                entry: CacheEntry = pickle.load(file)

            ####################################################
            # Version Check
            ####################################################

            if getattr(entry, "version", 0) != self.CACHE_VERSION:

                print("[WebCache] VERSION MISMATCH")

                path.unlink(missing_ok=True)

                return None

            ####################################################
            # Update Last Access
            ####################################################

            entry.touch()

            ####################################################
            # Save Updated Metadata
            ####################################################

            with open(path, "wb") as file:

                pickle.dump(entry, file)

            print("[WebCache] HIT")

            return entry

        except Exception as e:

            print(f"[WebCache] Corrupted cache: {e}")

            try:

                path.unlink()

            except Exception:

                pass

            return None

    ############################################################

    def save(

        self,

        url: str,

        title: str,

        chunks

    ):

        entry = CacheEntry(

            url=url,

            title=title,

            chunks=chunks,

            version=self.CACHE_VERSION

        )

        path = self._filename(url)

        with open(path, "wb") as file:

            pickle.dump(entry, file)

        print("[WebCache] SAVED")

    ############################################################

    def clear(self):

        count = 0

        for file in self.CACHE_DIR.glob("*.pkl"):

            try:

                file.unlink()

                count += 1

            except Exception:

                pass

        print(f"[WebCache] Cleared {count} files.")

    ############################################################

    def stats(self):

        files = list(

            self.CACHE_DIR.glob("*.pkl")

        )

        total = sum(

            file.stat().st_size

            for file in files

        )

        return {

            "entries": len(files),

            "size_bytes": total,

            "size_mb": round(

                total / (1024 * 1024),

                2

            )

        }