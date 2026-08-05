import re


class HeadingDetector:
    """
    Detect probable section headings.
    """

    ROMAN = re.compile(r"^[IVXLCDM]+\.$")

    NUMBERED = re.compile(r"^\d+(\.\d+)*")

    def is_heading(self, line: str) -> bool:

        line = line.strip()

        if not line:
            return False

        if len(line) > 90:
            return False

        if line.endswith(":"):
            return True

        if self.NUMBERED.match(line):
            return True

        if self.ROMAN.match(line):
            return True

        words = line.split()

        if len(words) <= 8:

            uppercase = sum(
                w[0].isupper()
                for w in words
                if w
            )

            if uppercase >= len(words) * 0.6:
                return True

        return False