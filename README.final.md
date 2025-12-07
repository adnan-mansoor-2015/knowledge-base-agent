# Super Call Center Agent (SCCA)

A comprehensive project to build an advanced, intelligent agent capable of handling complex retrieval and conversational tasks. This project evolves from a simple RAG pipeline to a sophisticated, self-correcting agent using LangChain and LangGraph.

## Project Phases

### Phase 1: Foundational Data and Linear RAG Pipeline
**Goal:** Establish the reliable base for data ingestion and a simple, highly efficient Retrieval-Augmented Generation (RAG) chain using core LangChain components.

#### 1.1 Data Ingestion & Indexing
-   **Concepts:** Chunking, Embedding Models, Vector Representations, Cosine Similarity.
-   **Deliverable:** A functional Vector Store populated with company documents (e.g., 10-K, FAQs).
-   **Implementation:**
    -   Split documents using `RecursiveCharacterTextSplitter`.
    -   Embed and store in a vector database.
    -   Verify with a test query (e.g., "When was our last product launched?") to retrieve top-3 relevant chunks.

#### 1.2 Core RAG Chain (LCEL)
-   **Concepts:** LCEL, Runnables, ChatPromptTemplate, LLM.
-   **Deliverable:** A single, testable `Simple_RAG_Chain`.
-   **Structure:** `retriever | prompt | llm | parser`.

#### 1.3 Tool Definition & Readiness
-   **Concepts:** Tools, RunSerializable.
-   **Deliverable:**
    -   `rag_lookup(query)`: Calls the RAG chain.
    -   `stock_lookup(ticker)`: Placeholder for financial data.
    -   Ensure both are `RunSerializable` for future Agent integration.

#### 1.4 Performance Baseline
-   **Concepts:** Transformers.
-   **Deliverable:** Initial measurement of latency (time to first token) for the `Simple_RAG_Chain` to establish a performance benchmark.

---

## Roadmap

### Phase 2: Agentic Orchestration and Conversational Memory
**Goal:** Introduce decision-making intelligence by enabling the small LLM to select tools and maintain multi-turn conversation context.
-   **2.1 Agent Assembly:** Define "Lead Analyst" Agent with tool access using `.bind_tools()`.
-   **2.2 Agent Execution Loop:** Manage multi-step thought-action-observation loops.
-   **2.3 Memory Integration:** Add `ConversationBufferMemory` for context awareness (e.g., resolving "there" to a previously mentioned entity).
-   **2.4 Concurrent Data Fetch:** Use `RunnableParallel` for complex queries requiring multiple tools simultaneously.

### Phase 3: Advanced RAG and Retrieval Optimization
**Goal:** Drastically improve retrieval quality for complex queries using LLM-based transformations.
-   **3.1 RAG Fusion:** Implement Query Translation and Reciprocal Rank Fusion.
-   **3.2 Complex Query Strategies:** utilizing Decomposition, HyDE, or Step-Back prompting.
-   **3.3 Adaptive Routing:** Classify intents (Financial, Knowledge, ChitChat) to optimize routing.
-   **3.4 Multi-Representation Indexing:** Summary indexing for better context retrieval.

### Phase 4: Self-Correction, Streaming, and Final Model
**Goal:** Implement the final, robust agentic flow (LangGraph) and optimize for deployment.
-   **4.1 LangGraph State Machine:** CRAG (Corrective RAG) implementation with confidence checks and query rewriting.
-   **4.2 Transparency and UX:** Streaming responses and `QueueCallbackHandler` for visible "thought" logs.
-   **4.3 Domain-Specific Fine-Tuning:** QLoRA/P-Tuning on organization-specific datasets.
-   **4.4 Deployment Readiness:** Optimization with KV Cache and `RunSerializable` workflows.