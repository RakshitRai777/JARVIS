from difflib import SequenceMatcher

from ai.tools.vision.ocr_element import OCRElement


class TextLocator:
    """
    Locates text within OCR results.

    This class performs text searching over OCR
    elements and returns the best matching
    OCRElement.

    Future versions may support fuzzy matching,
    regex, regions, confidence thresholds,
    and spatial relationships.
    """

    ############################################################

    def find_exact(
        self,
        elements: list[OCRElement],
        target: str,
    ) -> OCRElement | None:
        """
        Finds an exact text match.
        """

        target = target.lower().strip()

        for element in elements:

            if element.text.lower().strip() == target:

                return element

        return None

    ############################################################

    def find_contains(
        self,
        elements: list[OCRElement],
        target: str,
    ) -> OCRElement | None:
        """
        Finds the first OCR element containing
        the target text.
        """

        target = target.lower().strip()

        for element in elements:

            if target in element.text.lower():

                return element

        return None

    ############################################################

    def find_all(
        self,
        elements: list[OCRElement],
        target: str,
    ) -> list[OCRElement]:
        """
        Returns every OCR element containing
        the target text.
        """

        target = target.lower().strip()

        matches = []

        for element in elements:

            if target in element.text.lower():

                matches.append(element)

        return matches

    ############################################################

    def find_best_match(
        self,
        elements: list[OCRElement],
        target: str,
        threshold: float = 0.65,
    ) -> OCRElement | None:
        """
        Finds the closest text match using
        fuzzy similarity.
        """

        target = target.lower().strip()

        best = None

        best_score = 0.0

        for element in elements:

            score = SequenceMatcher(

                None,

                target,

                element.text.lower(),

            ).ratio()

            if score > best_score:

                best_score = score

                best = element

        if best_score >= threshold:

            return best

        return None

    ############################################################

    def exists(
        self,
        elements: list[OCRElement],
        target: str,
    ) -> bool:
        """
        Returns True if the target exists.
        """

        return self.find_contains(

            elements,

            target,

        ) is not None