from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

from config import CHUNK_SIZE, CHUNK_OVERLAP


class DocumentChunker:
    """
    Splits LangChain Document objects into
    smaller chunks for semantic search.
    """

    def __init__(
        self,
        chunk_size: int = CHUNK_SIZE,
        chunk_overlap: int = CHUNK_OVERLAP,
    ):

        if chunk_overlap >= chunk_size:
            raise ValueError(
                "chunk_overlap must be smaller than chunk_size."
            )

        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,
            length_function=len,
            add_start_index=True,
        )

    def split(self, documents: list[Document]) -> list[Document]:
        """
        Split documents into smaller chunks while
        preserving metadata.
        """

        chunks = self.text_splitter.split_documents(documents)

        return chunks

    def summary(self, documents: list[Document], chunks: list[Document]):

        print("\n" + "=" * 70)
        print("CHUNKING SUMMARY")
        print("=" * 70)

        print(f"Documents Loaded : {len(documents)}")
        print(f"Chunks Created   : {len(chunks)}")

        avg_length = sum(len(chunk.page_content) for chunk in chunks) / len(chunks)

        print(f"Average Chunk Size : {avg_length:.2f} characters")

        print("=" * 70)

    def preview(
        self,
        chunks: list[Document],
        num_chunks: int = 3,
    ):
        """
        Preview the first few chunks.
        """

        print("\n")
        print("=" * 80)
        print("CHUNK PREVIEW")
        print("=" * 80)

        for index, chunk in enumerate(chunks[:num_chunks], start=1):

            print(f"\nChunk {index}")

            print("-" * 80)

            print(chunk.page_content)

            print("\nMetadata")

            print(chunk.metadata)

            print("=" * 80)