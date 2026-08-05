import re


class ContentCleaner:
    """
    Cleans parsed webpage text.

    Responsibilities
    ----------------
    • Remove citations
    • Remove navigation text
    • Remove advertisements
    • Remove metadata
    • Remove external links section
    • Remove references section
    • Normalize whitespace
    """

    def clean(
        self,
        text: str
    ) -> str:

        if not text:
            return ""

        ########################################################
        # Normalize line endings
        ########################################################

        text = text.replace("\r", "")

        ########################################################
        # Remove citation numbers
        ########################################################

        # [1]
        text = re.sub(
            r"\[\d+\]",
            "",
            text
        )

        # [ 12 ]
        text = re.sub(
            r"\[\s*\d+\s*\]",
            "",
            text
        )

        # Multiline citations:
        # [
        # 12
        # ]
        text = re.sub(
            r"\[\s*\n*\s*\d+\s*\n*\s*\]",
            "",
            text,
            flags=re.MULTILINE
        )

        ########################################################
        # Remove [edit]
        ########################################################

        text = re.sub(
            r"\[edit\]",
            "",
            text,
            flags=re.IGNORECASE
        )

        ########################################################
        # Remove repeated spaces
        ########################################################

        text = re.sub(
            r"[ \t]+",
            " ",
            text
        )

        ########################################################
        # Remove repeated blank lines
        ########################################################

        text = re.sub(
            r"\n{3,}",
            "\n\n",
            text
        )

        ########################################################
        # Remove markdown tables
        ########################################################

        text = re.sub(
            r"\|.*?\|",
            "",
            text
        )

        ########################################################
        # Split into lines
        ########################################################

        lines = text.splitlines()

        cleaned = []

        ########################################################
        # Ignore everything after these headings
        ########################################################

        stop_sections = {

            "references",
            "external links",
            "see also",
            "further reading",
            "notes",
            "bibliography"

        }

        ########################################################
        # Common navigation / promotional lines
        ########################################################

        blacklist = {

            "courses",
            "tutorials",
            "practice",
            "practice problems",
            "placement",
            "job board",
            "jobs",
            "share",
            "facebook",
            "twitter",
            "linkedin",
            "instagram",
            "youtube",
            "telegram",
            "whatsapp",
            "advertisement",
            "cookie policy",
            "privacy policy",
            "terms of service",
            "download pdf",
            "print",
            "jump to content",
            "toggle sidebar",
            "table of contents",
            "contents"

        }

        ########################################################

        for line in lines:

            line = line.strip()

            if not line:
                continue

            lower = line.lower()

            ####################################################
            # Stop parsing after references
            ####################################################

            if lower in stop_sections:
                break

            ####################################################
            # Remove promotional lines
            ####################################################

            if any(word in lower for word in blacklist):
                continue

            ####################################################
            # Ignore tiny UI fragments
            ####################################################

            if len(line) < 3:
                continue

            cleaned.append(line)

        ########################################################

        text = "\n\n".join(cleaned)

        ########################################################
        # Final whitespace normalization
        ########################################################

        text = re.sub(
            r"\n{3,}",
            "\n\n",
            text
        )

        return text.strip()