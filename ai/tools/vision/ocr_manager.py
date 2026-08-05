import easyocr


class OCRManager:
    """
    Handles Optical Character Recognition (OCR).

    Loads the OCR model once and reuses it.
    """

    ############################################################

    def __init__(self):

        self.reader = easyocr.Reader(

            ["en"],

            gpu=False,

        )

    ############################################################

    def extract_text(
        self,
        image_path: str,
    ) -> str:

        results = self.reader.readtext(

            image_path,

            detail=0,

        )

        return "\n".join(results)