from config import PDF_DIR

from src.ingestion.loader import PDFLoader
from src.ingestion.chunker import DocumentChunker


def main():

    pdf_path = PDF_DIR / "battery.pdf"

    loader = PDFLoader(str(pdf_path))
    documents = loader.load()

    chunker = DocumentChunker()

    chunks = chunker.split(documents)

    chunker.summary(documents, chunks)

    chunker.preview(chunks, num_chunks=5)


if __name__ == "__main__":
    main()