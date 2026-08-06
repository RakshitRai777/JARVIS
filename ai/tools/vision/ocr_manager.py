import easyocr

from ai.tools.vision.ocr_element import OCRElement


class OCRManager:
    """
    Handles Optical Character Recognition.

    Loads the OCR model once and returns
    structured OCR elements.
    """

    ############################################################

    def __init__(self):

        self.reader = None

    ############################################################

    def _get_reader(self):
        if self.reader is None:
            self.reader = easyocr.Reader(
                ["en"],
                gpu=False,
            )
        return self.reader

    ############################################################

    def extract_elements(
        self,
        image_path: str,
    ) -> list[OCRElement]:

        """
        Returns every OCR detection.
        """

        results = self._get_reader().readtext(

            image_path,

            detail=1,

        )

        elements = []

        for bbox, text, confidence in results:

            elements.append(

                OCRElement(

                    text=text,

                    confidence=float(confidence),

                    bbox=bbox,

                )

            )

        return elements

    ############################################################

    def extract_text(
        self,
        image_path: str,
    ) -> str:
        """
        Convenience wrapper.

        Returns plain text built from OCR
        elements.
        """

        elements = self.extract_elements(

            image_path

        )

        return "\n".join(

            element.text

            for element in elements

        )