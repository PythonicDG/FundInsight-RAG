import chromadb
from chromadb.utils import embedding_functions


emb_fn = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")


collection = chroma_client.get_or_create_collection(
    name="journal_entries",
    embedding_function=emb_fn
)

with open("data/small_cap_factsheet.txt", "r") as f:
    text = f.read()

raw_chunks = text.split("##")

chunks = [chunk.strip() for chunk in raw_chunks if chunk.strip()]

print(chunks[0])