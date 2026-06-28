from config import PDF_DIR
from src.ingestion.loader import PDFLoader


def main():

    pdf_path = PDF_DIR / "battery.pdf"

    loader = PDFLoader(str(pdf_path))

    documents = loader.load()

    print("=" * 80)
    print("PDF LOADER TEST")
    print("=" * 80)

    print(f"\nTotal Pages : {len(documents)}\n")

    for index, document in enumerate(documents, start=1):

        print(f"Page {index}")
        print("-" * 80)

        print(document.page_content[:300])

        print("\nMetadata")

        print(document.metadata)

        print("=" * 80)


if __name__ == "__main__":
    main()