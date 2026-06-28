from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document


class PDFLoader:
    """
    Loads PDF documents and returns LangChain Document objects.
    """

    def __init__(self, pdf_path: str):
        self.pdf_path = Path(pdf_path)

        if not self.pdf_path.exists():
            raise FileNotFoundError(
                f"PDF not found: {self.pdf_path.resolve()}"
            )

    def load(self) -> list[Document]:
        loader = PyPDFLoader(str(self.pdf_path))
        return loader.load()