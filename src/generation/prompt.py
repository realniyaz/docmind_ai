class PromptBuilder:

    @staticmethod
    def build(context: str, question: str):

        return f"""
You are an expert AI assistant.

Answer ONLY using the provided context.

If the answer is not found in the context,
reply:

"I couldn't find the answer in the provided document."

-------------------------
Context
-------------------------

{context}

-------------------------
Question
-------------------------

{question}

-------------------------
Answer
-------------------------
"""