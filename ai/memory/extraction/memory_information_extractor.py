import re


class MemoryInformationExtractor:
    """
    Extracts structured information from memories.

    Output
    ------
    category
    subject
    value
    """

    ############################################################

    PREFERENCE_PATTERNS = [

        r"(?:remember that )?my (.+?) is (.+)",

        r"i like (.+)",

        r"i love (.+)",

        r"my favourite (.+?) is (.+)",

        r"my favorite (.+?) is (.+)",

    ]

    ############################################################

    def extract(self, text: str):

        text = text.strip()

        ########################################################
        # Preferences
        ########################################################

        for pattern in self.PREFERENCE_PATTERNS:

            match = re.match(

                pattern,

                text,

                re.IGNORECASE,

            )

            if not match:
                continue

            ####################################################

            groups = match.groups()

            ####################################################

            if len(groups) == 2:

                return {

                    "category": "preference",

                    "subject": groups[0].strip(),

                    "value": groups[1].strip(),

                }

            ####################################################

            if len(groups) == 1:

                return {

                    "category": "preference",

                    "subject": "likes",

                    "value": groups[0].strip(),

                }

        ########################################################

        return {

            "category": None,

            "subject": None,

            "value": None,

        }