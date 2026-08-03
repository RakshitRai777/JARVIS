import re


class ContentCleaner:
    """
    Cleans parsed webpage text.

    Removes:
    - Wikipedia citations ([1], [25], ...)
    - [edit]
    - [citation needed]
    - Markdown table rows
    - Multiple spaces
    - Excessive blank lines
    """

    def clean(self, text: str) -> str:

        if not text:
            return ""

        # ----------------------------------------
        # Remove citation numbers
        # Example: [1], [25], [123]
        # ----------------------------------------
        text = re.sub(
            r"\[\d+\]",
            "",
            text,
        )

        # ----------------------------------------
        # Remove [edit]
        # ----------------------------------------
        text = re.sub(
            r"\[edit\]",
            "",
            text,
            flags=re.IGNORECASE,
        )

        # ----------------------------------------
        # Remove [citation needed]
        # ----------------------------------------
        text = re.sub(
            r"\[citation needed\]",
            "",
            text,
            flags=re.IGNORECASE,
        )

        # ----------------------------------------
        # Remove markdown table rows
        # Example:
        # | Header |
        # |-------|
        # ----------------------------------------
        text = re.sub(
            r"^\|.*$",
            "",
            text,
            flags=re.MULTILINE,
        )

        # ----------------------------------------
        # Remove markdown separators
        # ----------------------------------------
        text = re.sub(
            r"^-{3,}$",
            "",
            text,
            flags=re.MULTILINE,
        )

        # ----------------------------------------
        # Remove multiple spaces/tabs
        # ----------------------------------------
        text = re.sub(
            r"[ \t]+",
            " ",
            text,
        )

        # ----------------------------------------
        # Remove trailing spaces before newlines
        # ----------------------------------------
        text = re.sub(
            r" *\n",
            "\n",
            text,
        )

        # ----------------------------------------
        # Collapse multiple blank lines
        # ----------------------------------------
        text = re.sub(
            r"\n\s*\n+",
            "\n\n",
            text,
        )

        # ----------------------------------------
        # Remove excessive newlines
        # ----------------------------------------
        text = re.sub(
            r"\n{3,}",
            "\n\n",
            text,
        )

        return text.strip()