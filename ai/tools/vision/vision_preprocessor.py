import re


class VisionPreprocessor:
    """
    Cleans and normalizes OCR output.

    Every Vision tool should use this class
    before sending text to an LLM.
    """

    ############################################################

    def preprocess(
        self,
        text: str,
    ) -> str:

        if not text:

            return ""

        text = self._normalize_newlines(text)

        text = self._remove_empty_lines(text)

        text = self._normalize_spaces(text)

        text = self._merge_wrapped_lines(text)

        text = self._remove_duplicate_lines(text)

        text = self._remove_noise(text)

        return text.strip()

    ############################################################

    def _normalize_newlines(
        self,
        text: str,
    ) -> str:

        return text.replace("\r\n", "\n").replace("\r", "\n")

    ############################################################

    def _remove_empty_lines(
        self,
        text: str,
    ) -> str:

        lines = []

        for line in text.split("\n"):

            line = line.strip()

            if line:

                lines.append(line)

        return "\n".join(lines)

    ############################################################

    def _normalize_spaces(
        self,
        text: str,
    ) -> str:

        text = re.sub(
            r"[ \t]+",
            " ",
            text,
        )

        return text

    ############################################################

    def _merge_wrapped_lines(
        self,
        text: str,
    ) -> str:

        lines = text.split("\n")

        merged = []

        i = 0

        while i < len(lines):

            current = lines[i]

            if (

                i + 1 < len(lines)

                and len(current) < 20

                and len(lines[i + 1]) < 20

            ):

                merged.append(

                    current + " " + lines[i + 1]

                )

                i += 2

            else:

                merged.append(current)

                i += 1

        return "\n".join(merged)

    ############################################################

    def _remove_duplicate_lines(
        self,
        text: str,
    ) -> str:

        seen = set()

        cleaned = []

        for line in text.split("\n"):

            key = line.lower()

            if key not in seen:

                seen.add(key)

                cleaned.append(line)

        return "\n".join(cleaned)

    ############################################################

    def _remove_noise(
        self,
        text: str,
    ) -> str:

        cleaned = []

        for line in text.split("\n"):

            stripped = line.strip()

            ####################################################
            # Skip tiny OCR garbage
            ####################################################

            if len(stripped) <= 1:

                continue

            ####################################################
            # Skip lines containing only punctuation
            ####################################################

            if re.fullmatch(

                r"[\W_]+",

                stripped,

            ):

                continue

            ####################################################
            # Skip isolated numbers
            ####################################################

            if re.fullmatch(

                r"\d+",

                stripped,

            ):

                continue

            cleaned.append(stripped)

        return "\n".join(cleaned)