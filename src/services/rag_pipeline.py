from pathlib import Path

from config import PDF_DIR

from src.ingestion.loader import PDFLoader
from src.ingestion.chunker import DocumentChunker
from src.embedding.embeddings import EmbeddingModel
from src.retrieval.vectordb import VectorDatabase
from src.retrieval.retriever import Retriever
from src.generation.prompt import PromptBuilder
from src.generation.llm import LLM


class RAGPipeline:
    """
    Complete RAG Pipeline

    Responsibilities:
    -----------------
    1. Load PDF
    2. Chunk PDF
    3. Store embeddings in ChromaDB
    4. Retrieve relevant chunks
    5. Build prompt
    6. Generate final answer
    """

    def __init__(self):

        print("=" * 70)
        print("🚀 Initializing RAG Pipeline")
        print("=" * 70)

        # Initialize reusable components only once
        self.chunker = DocumentChunker()

        self.embedding_model = EmbeddingModel().get_model()

        self.vector_db = VectorDatabase(
            self.embedding_model
        )

        self.llm = LLM()

        self.retriever = None

        print("✅ Pipeline Ready!\n")

    # ==========================================================
    # INDEXING
    # ==========================================================

    def index_pdf(self, pdf_name: str):

        pdf_path = PDF_DIR / pdf_name

        if not pdf_path.exists():
            raise FileNotFoundError(
                f"PDF not found : {pdf_path}"
            )

        print("=" * 70)
        print("📄 INDEXING PDF")
        print("=" * 70)

        print(f"Loading : {pdf_name}")

        loader = PDFLoader(str(pdf_path))

        documents = loader.load()

        print(f"Loaded {len(documents)} pages")

        print("\nChunking document...")

        chunks = self.chunker.split(documents)

        print(f"Generated {len(chunks)} chunks")

        print("\nResetting Vector Database...")

        self.vector_db.reset()

        print("Storing embeddings...")

        self.vector_db.add_documents(chunks)

        total_chunks = self.vector_db.count()

        print(f"Stored {total_chunks} chunks")

        self.retriever = Retriever(self.vector_db)

        print("\n✅ PDF Indexed Successfully")

        return total_chunks

    # ==========================================================
    # CONTEXT FORMATTER
    # ==========================================================

    def format_context(self, documents):

        context = []

        for doc in documents:

            context.append(doc.page_content)

        return "\n\n".join(context)

    # ==========================================================
    # ASK QUESTION
    # ==========================================================

    def ask(self, question: str):

        if self.retriever is None:

            raise ValueError(
                "Please index a PDF before asking questions."
            )

        print("\nSearching Vector Database...")

        documents = self.retriever.retrieve(question)

        print(f"Retrieved {len(documents)} documents")

        context = self.format_context(documents)

        prompt = PromptBuilder.build(
            context=context,
            question=question
        )

        print("Generating Answer...\n")

        answer = self.llm.generate(prompt)

        sources = []

        for doc in documents:

            metadata = doc.metadata

            sources.append({
                "page": metadata.get("page", "Unknown"),
                "source": Path(
                    metadata.get("source", "")
                ).name
            })

        return {

            "question": question,

            "answer": answer,

            "sources": sources,

            "documents": documents,

            "context": context

        }

    # ==========================================================
    # CHAT LOOP
    # ==========================================================

    def chat(self):

        print("=" * 70)
        print("🤖 LOCAL RAG CHATBOT")
        print("=" * 70)

        print("Type 'exit' anytime.\n")

        while True:

            question = input("You : ")

            if question.lower() == "exit":

                print("\nGoodbye 👋")

                break

            result = self.ask(question)

            print("\nAI")
            print("-" * 70)

            print(result["answer"])

            print("\nSources")

            for source in result["sources"]:

                print(
                    f"- {source['source']} | Page {source['page'] + 1}"
                )

            print("\n" + "=" * 70)