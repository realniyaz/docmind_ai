from langchain_chroma import Chroma
from config import CHROMA_DB_DIR, COLLECTION_NAME


class VectorDatabase:

    def __init__(self, embedding_model):

        self.db = Chroma(
            collection_name=COLLECTION_NAME,
            embedding_function=embedding_model,
            persist_directory=str(CHROMA_DB_DIR),
        )

    def add_documents(self, documents):
        self.db.add_documents(documents)

    def get_retriever(self, k=4):
        return self.db.as_retriever(search_kwargs={"k": k})

    def count(self):
        return self.db._collection.count()

    def reset(self):
        self.db.reset_collection()