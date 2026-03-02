import chromadb
from chromadb.utils import embedding_functions

chroma_client = chromadb.Client()

emb_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

collection = chroma_client.get_or_create_collection(
    name="small_cap_fund",
    embedding_function=emb_fn
)

with open("data/small_cap_factsheet.txt", "r", encoding="utf-8") as f:
    text = f.read()

raw_chunks = text.split("##")
chunks = [chunk.strip() for chunk in raw_chunks if chunk.strip()]

collection.add(
    documents=chunks,
    ids=[f"id_{i}" for i in range(len(chunks))]
)
