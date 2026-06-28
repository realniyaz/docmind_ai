from src.rag_pipeline import RAGPipeline


def main():

    pipeline = RAGPipeline()

    pipeline.index_pdf("battery.pdf")

    print("\n" + "=" * 70)
    print("RAG Chatbot Ready!")
    print("Type 'exit' to quit.")
    print("=" * 70)

    while True:

        question = input("\nAsk: ")

        if question.lower() == "exit":
            print("\nGoodbye!")
            break

        result = pipeline.ask(question)

        print("\nAnswer:")
        print("-" * 70)

        print(result["answer"])


if __name__ == "__main__":
    main()