from langchain_core.documents import Document


class Retriever:
    """
    Handles semantic retrieval from the vector database.
    """

    def __init__(self, vector_db):

        self.retriever = vector_db.get_retriever(k=4)

    def retrieve(self, query: str) -> list[Document]:

        documents = self.retriever.invoke(query)

        return documents