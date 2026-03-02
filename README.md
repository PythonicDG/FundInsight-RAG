# 📈 FundInsight: Intelligent Financial RAG Dashboard

**FundInsight** is a Retrieval-Augmented Generation (RAG) application designed to help financial analysts quickly extract insights from complex mutual fund factsheets. Instead of manually searching through pages of PDF/text data, you can simply ask questions in natural language and get instant, context-aware answers.

---

## 🚀 Key Features

- **Instant Insights**: Ask questions like *"What are the top sector allocations?"* or *"Who is the fund manager?"* and get precise answers.
- **Smart Retrieval**: Uses **ChromaDB** and **Sentence Transformers** to perform semantic search, meaning it understands the *meaning* of your questions, not just keywords.
- **Persistent Memory**: The system remembers your indexed data, so it doesn't need to rebuild the database every time you start the app.
- **Modern Dashboard**: A clean, professional interface built with **Streamlit** for a premium user experience.

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Vector Database**: ChromaDB
- **Embeddings**: Sentence-Transformers (`all-MiniLM-L6-v2`)
- **Backend**: Python

---

## 📦 Getting Started

### 1. Installation
First, clone the repository and navigate to the project folder. Create a virtual environment and install the required packages:

```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate

# Install dependencies
pip install streamlit chromadb sentence-transformers
```

### 2. Running the App
Launch the dashboard with a single command:

```bash
streamlit run app.py
```

---

## 💡 How It Works (The "RAG" Magic)

1. **Indexing**: The app reads the `small_cap_factsheet.txt`, breaks it into logical chunks, and converts those chunks into high-dimensional "vectors" (embeddings).
2. **Storage**: These vectors are stored in a **ChromaDB** collection.
3. **Retrieval**: When you ask a question, the app converts your question into a vector and finds the "closest" matches in the database.
4. **Presentation**: The most relevant insights are displayed neatly in the dashboard cards.

---

## 📂 Project Structure

- `app.py`: The heart of the application (Streamlit logic).
- `data/`: Contains the source financial factsheets.
- `chroma_db/`: Persistent storage for indexed data.
- `venv/`: Your local Python environment.

---

## 👤 Author
Developed as a demonstration of **Agentic AI** and **Financial Data Engineering**. 
Suitable for showcasing in portfolios for roles involving Data Science, AI Engineering, or Fintech.
