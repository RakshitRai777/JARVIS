import re

from ai.web.intent.intent_classifier import IntentClassifier
from ai.web.intent.search_intent import SearchIntent
from ai.web.query_expander.expanded_query import ExpandedQuery
from ai.web.query_expander.question_pattern import QuestionPattern
from ai.web.query_expander.question_pattern_detector import (
    QuestionPatternDetector,
)


class QueryExpander:
    """
    Expands a query according to both its SearchIntent
    and QuestionPattern.

    Pipeline
    --------
    Query
        ↓
    Intent Classification
        ↓
    Question Pattern Detection
        ↓
    Intent-specific Expansion
    """

    MAX_QUERIES = 5

    ############################################################

    def __init__(self):

        self.classifier = IntentClassifier()

        self.pattern_detector = QuestionPatternDetector()

    ############################################################

    def expand(
        self,
        query: str,
    ) -> ExpandedQuery:

        original = query.strip()

        normalized = original.lower().strip()

        intent = self.classifier.classify(normalized)

        pattern = self.pattern_detector.detect(normalized)

        queries = [original]

        ########################################################
        # PERSON
        ########################################################

        if intent == SearchIntent.PERSON:

            subject = normalized

            subject = re.sub(
                r"\b(who|is|was|the|a|an|of)\b",
                "",
                subject,
            )

            subject = re.sub(r"\?", "", subject)

            subject = " ".join(subject.split())

            ####################################################
            # Creator
            ####################################################

            if pattern == QuestionPattern.CREATOR:

                subject = re.sub(
                    r"\b(created|creator|developed|made)\b",
                    "",
                    subject,
                ).strip()

                queries.extend([

                    f"{subject} creator",

                    f"{subject} inventor",

                    f"{subject} history",

                    f"{subject} wikipedia",

                ])

            ####################################################
            # Inventor
            ####################################################

            elif pattern == QuestionPattern.INVENTOR:

                subject = re.sub(
                    r"\b(invented|inventor)\b",
                    "",
                    subject,
                ).strip()

                queries.extend([

                    f"{subject} inventor",

                    f"{subject} creator",

                    f"{subject} history",

                    f"{subject} wikipedia",

                ])

            ####################################################
            # CEO
            ####################################################

            elif pattern == QuestionPattern.CEO:

                subject = re.sub(
                    r"\b(ceo|chief executive officer)\b",
                    "",
                    subject,
                ).strip()

                queries.extend([

                    f"{subject} CEO",

                    f"{subject} chief executive officer",

                    f"{subject} leadership",

                    f"{subject} official",

                ])

            ####################################################
            # Founder
            ####################################################

            elif pattern == QuestionPattern.FOUNDER:

                subject = re.sub(
                    r"\b(founder|founded)\b",
                    "",
                    subject,
                ).strip()

                queries.extend([

                    f"{subject} founder",

                    f"{subject} company history",

                    f"{subject} official",

                    f"{subject} wikipedia",

                ])

            ####################################################
            # Author
            ####################################################

            elif pattern == QuestionPattern.AUTHOR:

                subject = re.sub(
                    r"\b(author|wrote|written)\b",
                    "",
                    subject,
                ).strip()

                queries.extend([

                    f"{subject} author",

                    f"{subject} books",

                    f"{subject} bibliography",

                    f"{subject} wikipedia",

                ])

            ####################################################
            # Birth
            ####################################################

            elif pattern == QuestionPattern.BIRTH:

                subject = re.sub(
                    r"\b(where|born)\b",
                    "",
                    subject,
                ).strip()

                queries.extend([

                    f"{subject} birthplace",

                    f"{subject} biography",

                    f"{subject} wikipedia",

                    f"{subject} early life",

                ])

            ####################################################
            # Death
            ####################################################

            elif pattern == QuestionPattern.DEATH:

                queries.extend([

                    f"{subject} death",

                    f"{subject} biography",

                    f"{subject} wikipedia",

                    f"{subject} legacy",

                ])

            ####################################################
            # Default PERSON
            ####################################################

            else:

                queries.extend([

                    f"{subject} wikipedia",

                    f"{subject} biography",

                    f"{subject} official",

                ])

        ########################################################
        # NEWS
        ########################################################

        elif intent == SearchIntent.NEWS:

            base = normalized

            base = re.sub(
                r"\b(latest|news)\b",
                "",
                base,
            ).strip()

            queries.extend([

                f"{base} latest news",

                f"{base} today",

                f"{base} updates",

                f"{base} official news",

            ])

        ########################################################
        # PRODUCT
        ########################################################

        elif intent == SearchIntent.PRODUCT:

            queries.extend([

                f"{normalized} specifications",

                f"{normalized} benchmark",

                f"{normalized} review",

                f"{normalized} comparison",

            ])

        ########################################################
        # SHOPPING
        ########################################################

        elif intent == SearchIntent.SHOPPING:

            queries.extend([

                f"{normalized} best price",

                f"{normalized} amazon",

                f"{normalized} flipkart",

                f"{normalized} review",

            ])

        ########################################################
        # TUTORIAL
        ########################################################

        elif intent == SearchIntent.TUTORIAL:

            queries.extend([

                f"{normalized} documentation",

                f"{normalized} tutorial",

                f"{normalized} examples",

                f"{normalized} guide",

            ])

        ########################################################
        # MEDICAL
        ########################################################

        elif intent == SearchIntent.MEDICAL:

            queries.extend([

                normalized,

                f"{normalized} mayo clinic",

                f"{normalized} who",

                f"{normalized} nhs",

            ])

        ########################################################
        # PROGRAMMING
        ########################################################

        elif intent == SearchIntent.PROGRAMMING:

            queries.extend([

                f"{normalized} documentation",

                f"{normalized} tutorial",

                f"{normalized} github",

                f"{normalized} examples",

            ])

        ########################################################
        # ENCYCLOPEDIA
        ########################################################

        elif intent == SearchIntent.ENCYCLOPEDIA:

            queries.extend([

                f"{normalized} wikipedia",

                f"{normalized} history",

                f"{normalized} britannica",

                f"{normalized} definition",

            ])

        ########################################################
        # GENERAL
        ########################################################

        else:

            queries.extend([

                normalized,

                f"{normalized} wikipedia",

                f"{normalized} official",

            ])

        ########################################################
        # Remove duplicates
        ########################################################

        unique = []

        seen = set()

        for q in queries:

            q = " ".join(q.split())

            key = q.lower()

            if key in seen:
                continue

            seen.add(key)

            unique.append(q)

        ########################################################

        unique = unique[: self.MAX_QUERIES]

        ########################################################

        print()

        print(f"[Intent] {intent.value}")

        print(f"[Pattern] {pattern.value}")

        ########################################################

        return ExpandedQuery(

            original_query=original,

            queries=unique,

            reason=(
                f"Intent={intent.value}, "
                f"Pattern={pattern.value}"
            ),

        )