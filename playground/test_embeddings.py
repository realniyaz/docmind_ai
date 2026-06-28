from src.embedding.embeddings import EmbeddingModel


embedding_model = EmbeddingModel().get_model()

text = "Lithium-ion batteries are rechargeable."

embedding = embedding_model.embed_query(text)

print(f"Embedding Dimension : {len(embedding)}")

print()

print(embedding[:10])