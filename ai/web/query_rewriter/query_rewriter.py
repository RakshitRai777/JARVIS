import re

from ai.web.query_rewriter.rewrite_result import RewriteResult


class QueryRewriter:
    """
    Intelligent Query Rewriter.

    Responsibilities
    ----------------
    • Normalize search queries
    • Expand abbreviations
    • Improve search wording
    • Preserve user intent

    Future
    ------
    • Conversation-aware rewriting
    • LLM rewriting
    • Domain-specific rewriting
    """

    ############################################################

    def __init__(self):

        self.replacements = {

            ####################################################
            # AI
            ####################################################

            " ai ": " artificial intelligence ",

            ####################################################
            # Programming
            ####################################################

            " python ": " python programming language ",

            " js ": " javascript ",

            " c++ ": " cpp ",

            ####################################################
            # Search wording
            ####################################################

            " made ": " created ",

            " invented ": " created ",

            " built ": " created ",

            " latest ": " current ",

            " newest ": " current ",

            " today ": " current ",

        }

    ############################################################

    def rewrite(

        self,

        query: str,

    ) -> RewriteResult:

        if not query:

            return RewriteResult(

                original_query="",

                rewritten_query="",

                changed=False,

                reason="Empty query."

            )

        ########################################################

        original = query.strip()

        rewritten = f" {original.lower()} "

        ########################################################
        # Apply replacements
        ########################################################

        for old, new in self.replacements.items():

            rewritten = rewritten.replace(

                old,

                new

            )

        ########################################################
        # Remove duplicate whitespace
        ########################################################

        rewritten = re.sub(

            r"\s+",

            " ",

            rewritten

        ).strip()

        ########################################################

        changed = rewritten != original.lower()

        ########################################################

        if changed:

            reason = "Query normalized."

        else:

            reason = "No rewrite needed."

        ########################################################

        return RewriteResult(

            original_query=original,

            rewritten_query=rewritten,

            changed=changed,

            reason=reason

        )