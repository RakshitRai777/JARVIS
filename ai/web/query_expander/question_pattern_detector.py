import re

from ai.web.query_expander.question_pattern import QuestionPattern


class QuestionPatternDetector:
    """
    Detects the type of question being asked.

    This is more specific than SearchIntent.

    Example

    Intent:
        PERSON

    Pattern:
        CEO

    Expansion:
        Google CEO
        Google leadership
    """

    ##########################################################

    def detect(
        self,
        query: str,
    ) -> QuestionPattern:

        q = query.lower()

        ######################################################
        # CEO
        ######################################################

        if re.search(
            r"\b(ceo|chief executive officer)\b",
            q,
        ):
            return QuestionPattern.CEO

        ######################################################
        # Founder
        ######################################################

        if re.search(
            r"\b(founder|founded)\b",
            q,
        ):
            return QuestionPattern.FOUNDER

        ######################################################
        # Creator
        ######################################################

        if re.search(
            r"\b(created|creator|developed|made)\b",
            q,
        ):
            return QuestionPattern.CREATOR

        ######################################################
        # Inventor
        ######################################################

        if re.search(
            r"\b(invented|inventor)\b",
            q,
        ):
            return QuestionPattern.INVENTOR

        ######################################################
        # Author
        ######################################################

        if re.search(
            r"\b(author|wrote|written)\b",
            q,
        ):
            return QuestionPattern.AUTHOR

        ######################################################
        # Birth
        ######################################################

        if re.search(
            r"\bwhere\b.*\bborn\b",
            q,
        ):
            return QuestionPattern.BIRTH

        ######################################################
        # Death
        ######################################################

        if re.search(
            r"\b(died|death|passed away)\b",
            q,
        ):
            return QuestionPattern.DEATH

        ######################################################
        # Release
        ######################################################

        if re.search(
            r"\b(released|release date|launched)\b",
            q,
        ):
            return QuestionPattern.RELEASE

        ######################################################
        # Tutorial
        ######################################################

        if re.search(
            r"\b(tutorial|learn|guide|how to)\b",
            q,
        ):
            return QuestionPattern.TUTORIAL

        ######################################################
        # Documentation
        ######################################################

        if re.search(
            r"\b(documentation|docs|api)\b",
            q,
        ):
            return QuestionPattern.DOCUMENTATION

        ######################################################
        # Review
        ######################################################

        if re.search(
            r"\b(review|reviews)\b",
            q,
        ):
            return QuestionPattern.REVIEW

        ######################################################
        # Comparison
        ######################################################

        if re.search(
            r"\b(compare|comparison|vs|versus)\b",
            q,
        ):
            return QuestionPattern.COMPARISON

        ######################################################
        # Price
        ######################################################

        if re.search(
            r"\b(price|cost|buy)\b",
            q,
        ):
            return QuestionPattern.PRICE

        ######################################################
        # Specifications
        ######################################################

        if re.search(
            r"\b(specifications|specs|benchmark)\b",
            q,
        ):
            return QuestionPattern.SPECIFICATIONS

        ######################################################
        # Latest News
        ######################################################

        if re.search(
            r"\b(latest|breaking|today|news)\b",
            q,
        ):
            return QuestionPattern.LATEST_NEWS

        ######################################################
        # Symptoms
        ######################################################

        if re.search(
            r"\bsymptoms?\b",
            q,
        ):
            return QuestionPattern.SYMPTOMS

        ######################################################
        # Treatment
        ######################################################

        if re.search(
            r"\btreatment\b",
            q,
        ):
            return QuestionPattern.TREATMENT

        ######################################################
        # Causes
        ######################################################

        if re.search(
            r"\bcauses?\b",
            q,
        ):
            return QuestionPattern.CAUSES

        ######################################################

        return QuestionPattern.GENERAL