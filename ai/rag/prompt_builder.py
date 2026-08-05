from ai.embeddings.chunk import Chunk


class PromptBuilder:
    """
    Builds grounded prompts for Retrieval-Augmented Generation (RAG).

    Responsibilities
    ----------------
    • Convert retrieved chunks into context
    • Tell the LLM to answer ONLY from that context
    • Include source information
    """

    ############################################################

    def build(

        self,

        question: str,

        chunks: list[Chunk],

    ) -> list[dict]:

        ########################################################
        # Build Context
        ########################################################

        context = []

        for index, chunk in enumerate(chunks, start=1):

            context.append(

                f"""
SOURCE {index}
Title : {chunk.title}
URL   : {chunk.source}

{chunk.text}
""".strip()

            )

        evidence = "\n\n" + ("=" * 60) + "\n\n"

        evidence = evidence.join(context)

        ########################################################

        system_prompt = """
You are J.A.R.V.I.S.

Answer the user's question ONLY using the provided sources.

Rules:

1. If the answer exists in the sources, answer naturally.

2. Combine information from multiple sources when useful.

3. Do NOT invent facts.

4. If the sources are insufficient, clearly say:

"I couldn't find enough reliable information."

5. At the end include:

Sources:
- Source 1
- Source 2
...

Be concise but complete.
""".strip()

        ########################################################

        user_prompt = f"""
Question:

{question}

Retrieved Sources:

{evidence}
""".strip()

        ########################################################

        return [

            {

                "role": "system",

                "content": system_prompt

            },

            {

                "role": "user",

                "content": user_prompt

            }

        ]