# Knowledge Base Agent

A RAG (Retrieval-Augmented Generation) agent built with **LangChain** that uses **Ollama** for local embeddings and inference.

## Features
- **Data Loading**: Fetches content from web pages (e.g., Lilian Weng's Agent post).
- **Indexing**: Splits text and creates embeddings using `nomic-embed-text`.
- **Vector Store**: Stores embeddings in a local **Chroma** database.
- **Retrieval**: Fetches relevant context for user queries.
- **Generation**: Answers questions using the `pielee/qwen3-4b-thinking-2507_q8` local LLM via Ollama.

## Prerequisites

1. **Python 3.12+**
2. **Ollama**: [Download and install Ollama](https://ollama.com/).

### Required Models
You must pull the specific models used by the agent:

```bash
# Embedding model
ollama pull nomic-embed-text

# Inference model (LLM)
ollama pull pielee/qwen3-4b-thinking-2507_q8
```

## Setup

1. **Clone the repository** (if applicable).

2. **Create and activate a virtual environment**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration**:
   The application uses a `.env` file for configuration.
   
   Create a `.env` file in the root directory:
   ```bash
   cp .env.example .env  # If example exists, otherwise create new
   ```
   
   Add the following variables (if needed for tracing, otherwise optional for local runs):
   ```env
   # LangSmith Tracing (Optional)
   LANGCHAIN_TRACING_V2=true
   LANGCHAIN_ENDPOINT=https://api.smith.langchain.com
   LANGCHAIN_API_KEY=<your-langchain-api-key>
   
   # OpenAI Key (Not used for inference, but might be required by some libs)
   OPENAI_API_KEY=<your-openai-key>
   
   # User Agent (Required to identify requests)
   USER_AGENT=KnowledgeBaseAgent/1.0
   ```

## Usage

Run the agent:

```bash
python main.py
```

The script will:
1. Load and index the documentation.
2. Initialize the RAG pipeline.
3. Ask a pre-defined question ("Summarize") and print the answer.