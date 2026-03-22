# 🚀 AI Research Assistant (RAG-Based System)

An AI-powered backend system that allows users to upload PDFs and ask intelligent questions based on document content using **Retrieval-Augmented Generation (RAG)**.

---

## 🧠 Project Overview

This project demonstrates how modern AI systems combine **Vector Databases, Embeddings, and LLMs** to provide context-aware answers instead of relying solely on pretrained knowledge.

Instead of guessing answers, the system retrieves relevant information from uploaded documents and uses it to generate accurate responses.

---

## ⚡ Key Features

* 📄 Upload and process PDF documents
* ✂️ Intelligent text chunking with overlap
* 🔢 Embedding generation using HuggingFace models
* 📦 Vector storage using FAISS
* 🔍 Semantic similarity search (meaning-based retrieval)
* 🤖 AI-generated answers using LLM
* ⚡ FastAPI backend with interactive Swagger UI
* 🆓 Fully local execution (no API dependency)

---

## 🏗️ System Architecture

```
User Input
   ↓
FastAPI Backend
   ↓
PDF Processing (PyPDFLoader)
   ↓
Text Chunking (CharacterTextSplitter)
   ↓
Embeddings (HuggingFace)
   ↓
FAISS Vector Database
   ↓
Similarity Search
   ↓
Context + Query
   ↓
LLM (GPT-2)
   ↓
Generated Answer
```

---

## 🔄 Workflow Explained

### 1️⃣ Document Upload

* User uploads a PDF using `/upload`
* File is saved temporarily (`temp.pdf`)

### 2️⃣ Text Extraction

* PDF content is extracted using PyPDFLoader

### 3️⃣ Text Chunking

* Large text is split into smaller chunks
* Overlap is added to preserve context

### 4️⃣ Embedding Generation

* Each chunk is converted into a vector using:

  * `all-MiniLM-L6-v2` model

### 5️⃣ Vector Storage

* Embeddings are stored in FAISS for similarity search

### 6️⃣ Query Processing

* User sends query via `/ask`
* Query is converted into embedding

### 7️⃣ Retrieval (RAG)

* FAISS finds most relevant chunks

### 8️⃣ Answer Generation

* Retrieved context + query → LLM
* LLM generates final answer

---

## 🛠️ Tech Stack

| Component    | Technology                          |
| ------------ | ----------------------------------- |
| Backend      | FastAPI                             |
| AI Framework | LangChain                           |
| Embeddings   | HuggingFace (sentence-transformers) |
| Vector DB    | FAISS                               |
| LLM          | HuggingFace Transformers (GPT-2)    |
| Language     | Python                              |

---

## 📂 Project Structure

```
ai-research-assistant/
│
├── main.py              # FastAPI backend
├── requirements.txt     # Dependencies
├── README.md            # Documentation
├── .gitignore           # Ignore sensitive files
└── temp.pdf             # Temporary file (auto-generated)
```

---

## ▶️ How to Run Locally

### 1. Clone the repository

```
git clone https://github.com/YOUR_USERNAME/ai-research-assistant.git
cd ai-research-assistant
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run the server

```
python -m uvicorn main:app --reload
```

### 4. Open Swagger UI

👉 http://127.0.0.1:8000/docs

---

## 🌐 API Endpoints

| Endpoint  | Method | Description                 |
| --------- | ------ | --------------------------- |
| `/upload` | POST   | Upload PDF document         |
| `/ask`    | POST   | Ask questions from document |

---

## 🧠 Key Concepts Implemented

### 🔹 Retrieval-Augmented Generation (RAG)

Enhances LLM responses by retrieving relevant document context before generating answers.

### 🔹 Embeddings

Converts text into vectors to enable semantic understanding.

### 🔹 Vector Database (FAISS)

Stores embeddings and performs similarity search.

### 🔹 Semantic Search

Finds relevant content based on meaning, not exact keywords.

### 🔹 Backend API Design

Handles request-response cycle using FastAPI.

---

## ⚠️ Limitations

* GPT-2 is a basic LLM (limited accuracy)
* No persistent storage (data resets on restart)
* No frontend UI (Swagger used for testing)
* Context length limitations

---

## 🚀 Future Improvements

* Integrate advanced LLMs (GPT-4 / Gemini)
* Add chat memory (conversation history)
* Build frontend UI (React / Next.js)
* Deploy on cloud (AWS / Render)
* Add authentication system
* Optimize retrieval pipeline

---

## 📸 Demo (Recommended)

Add screenshots or demo video here:

* Swagger UI
* Upload success
* Question answering

---

## 👨‍💻 Author

**Gaurav More**
AI/ML Engineer (Student)

---

## ⭐ Final Note

This project demonstrates a real-world AI system architecture combining backend engineering and machine learning concepts, making it suitable for internships and production-level understanding.

---
