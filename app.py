import streamlit as st
import chromadb
from chromadb.utils import embedding_functions
import os

st.set_page_config(page_title="FundInsight | RAG Dashboard", page_icon="📈", layout="wide")

st.markdown("""
<style>
    .main { background-color: #f8f9fa; }
    .stTextInput > div > div > input { font-size: 1.1rem; }
    .result-card {
        padding: 20px;
        border-radius: 10px;
        background-color: white;
        border-left: 5px solid #007bff;
        margin-bottom: 15px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .result-header { font-weight: bold; color: #007bff; margin-bottom: 10px; }
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def get_chroma_collection():
    """
    Initializes ChromaDB with persistent storage and the embedding function.
    Only runs once and caches the result for performance.
    """
    persist_directory = "chroma_db"
    client = chromadb.PersistentClient(path=persist_directory)
    
    emb_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
    
    collection = client.get_or_create_collection(
        name="small_cap_fund",
        embedding_function=emb_fn
    )
    
    if collection.count() == 0:
        populate_collection(collection)
        
    return collection

def populate_collection(collection):
    """
    Reads the factsheet, splits into chunks, and adds to ChromaDB.
    This only runs the very first time the app is launched.
    """
    factsheet_path = "data/small_cap_factsheet.txt"
    if os.path.exists(factsheet_path):
        with open(factsheet_path, "r", encoding="utf-8") as f:
            text = f.read()
        
        raw_chunks = text.split("##")
        chunks = [chunk.strip() for chunk in raw_chunks if chunk.strip()]
        
        collection.add(
            documents=chunks,
            ids=[f"id_{i}" for i in range(len(chunks))]
        )
        st.info("System Initialized: Factsheet indexed successfully.")
    else:
        st.error(f"Error: Could not find factsheet at {factsheet_path}")

def main():
    st.title("📈 FundInsight RAG Dashboard")
    st.markdown("### Intelligent Financial Factsheet Analysis")
    st.write("Ask any question about the **Small Cap Alpha Fund** to retrieve relevant information instantly.")
    
    collection = get_chroma_collection()
    
    query = st.text_input("Enter your question:", placeholder="e.g., What are the top sectors? or Who is the fund manager?")
    
    num_results = st.sidebar.slider("Number of results", 1, 5, 3)
    
    if query:
        with st.spinner("Analyzing factsheet..."):
            results = collection.query(
                query_texts=[query],
                n_results=num_results
            )
            
            st.markdown("---")
            st.subheader(f"Top {num_results} Insights Found:")
            
            for i, doc in enumerate(results['documents'][0]):
                st.markdown(f"""
                <div class="result-card">
                    <div class="result-header">Insight #{i+1}</div>
                    <div>{doc}</div>
                </div>
                """, unsafe_allow_html=True)
                
    # Sidebar Info
    with st.sidebar:
        st.header("About This App")
        st.write("""
        This is a **Retrieval-Augmented Generation (RAG)** system built for financial analysts. 
        It uses:
        - **Streamlit**: For the dashboard UI.
        - **ChromaDB**: For vector search and persistent storage.
        - **Sentence Transformers**: For high-quality semantic embeddings.
        """)
        st.divider()
        st.caption("Developed for Portfolio Demonstrations")

if __name__ == "__main__":
    main()
