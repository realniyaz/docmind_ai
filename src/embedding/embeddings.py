from langchain_huggingface import HuggingFaceEmbeddings

from config import EMBEDDING_MODEL


class EmbeddingModel:
    """
    Handles document and query embeddings.
    """

    def __init__(self):

        self.embedding_model = HuggingFaceEmbeddings(
            model_name=EMBEDDING_MODEL
        )

    def get_model(self):
        return self.embedding_model