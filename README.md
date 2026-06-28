# 🤖 DocMind AI

<p align="center">

</p>

<h3 align="center">
Private AI Document Assistant using Local RAG
</h3>

<p align="center">

Build your own AI-powered document assistant that runs entirely on your machine using Ollama, LangChain, ChromaDB, and Streamlit.

</p>

---

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python)

![LangChain](https://img.shields.io/badge/LangChain-RAG-00A67E?style=for-the-badge)

![Ollama](https://img.shields.io/badge/Ollama-Llama3.2-000000?style=for-the-badge)

![Streamlit](https://img.shields.io/badge/Streamlit-UI-FF4B4B?style=for-the-badge&logo=streamlit)

![ChromaDB](https://img.shields.io/badge/ChromaDB-VectorDB-6E56CF?style=for-the-badge)

![License](https://img.shields.io/badge/License-MIT-success?style=for-the-badge)

</p>

---

# 📖 Overview

**DocMind AI** is a production-ready **Retrieval-Augmented Generation (RAG)** application that transforms static PDF documents into an intelligent conversational AI assistant.

Instead of manually searching through hundreds of pages, users can upload documents and ask natural language questions. The application retrieves the most relevant information using semantic search and generates accurate answers using a locally running Large Language Model.

Unlike cloud-based AI tools, **DocMind AI performs every operation locally**, ensuring complete privacy, zero API costs, and full ownership of your data.

---

# ✨ Key Features

## 📄 Document Processing

- Upload PDF documents
- Automatic document parsing
- Intelligent text chunking
- Persistent indexing
- Fast semantic retrieval

---

## 🤖 AI Capabilities

- Natural Language Question Answering
- Context-Aware Responses
- Semantic Search
- Intelligent Summarization
- Key Insight Extraction
- Concept Explanation
- Study Note Generation
- Interview Question Generation

---

## 🔒 Privacy First

- 100% Offline
- No OpenAI API
- No Internet Required
- Local Vector Database
- Local LLM
- Complete Data Ownership

---

## ⚡ Performance

- Persistent ChromaDB Storage
- Fast Similarity Search
- Low Latency Responses
- Source Citation
- Efficient Retrieval Pipeline
- Optimized Embedding Search

---

# 🎯 Why DocMind AI?

Traditional document search requires users to manually browse hundreds of pages.

DocMind AI changes the workflow:

```text
Upload PDF
      │
      ▼
Index Document
      │
      ▼
Ask Questions
      │
      ▼
Retrieve Context
      │
      ▼
Generate Answer
      │
      ▼
Source Citation

This dramatically improves productivity while maintaining complete privacy.

---

# 🏗 System Architecture

```text
                        ┌─────────────────────┐
                        │     User Uploads    │
                        │        PDF          │
                        └──────────┬──────────┘
                                   │
                                   ▼
                        ┌─────────────────────┐
                        │    PDF Loader       │
                        └──────────┬──────────┘
                                   │
                                   ▼
                        ┌─────────────────────┐
                        │  Document Chunker   │
                        └──────────┬──────────┘
                                   │
                                   ▼
                        ┌─────────────────────┐
                        │ Embedding Model     │
                        │ MiniLM-L6-v2        │
                        └──────────┬──────────┘
                                   │
                                   ▼
                        ┌─────────────────────┐
                        │     ChromaDB        │
                        │  Vector Database    │
                        └──────────┬──────────┘
                                   │
                                   ▼
                     ┌────────────────────────────┐
                     │ User asks a Question       │
                     └─────────────┬──────────────┘
                                   │
                                   ▼
                        ┌─────────────────────┐
                        │ Similarity Search   │
                        └──────────┬──────────┘
                                   │
                                   ▼
                        ┌─────────────────────┐
                        │ Prompt Builder      │
                        └──────────┬──────────┘
                                   │
                                   ▼
                        ┌─────────────────────┐
                        │ Llama 3.2 (Ollama)  │
                        └──────────┬──────────┘
                                   │
                                   ▼
                        ┌─────────────────────┐
                        │ AI Generated Answer │
                        └─────────────────────┘
```

---

# 🧠 How Retrieval-Augmented Generation Works

DocMind AI follows the standard enterprise RAG architecture.

### Step 1 — Upload PDF

Users upload one or more PDF documents.

↓

### Step 2 — Document Parsing

The application extracts text from every page.

↓

### Step 3 — Intelligent Chunking

Large documents are split into smaller semantic chunks for accurate retrieval.

↓

### Step 4 — Embedding Generation

Each chunk is converted into a dense vector using:

```
all-MiniLM-L6-v2
```

↓

### Step 5 — Vector Storage

Vectors are stored inside **ChromaDB**.

↓

### Step 6 — User Query

The user asks a natural language question.

↓

### Step 7 — Semantic Search

The Retriever finds the most relevant chunks using cosine similarity.

↓

### Step 8 — Prompt Engineering

The retrieved chunks are combined with the user's question.

↓

### Step 9 — Answer Generation

The prompt is sent to **Llama 3.2** running locally through Ollama.

↓

### Step 10 — Final Response

The user receives an accurate response with supporting context from the uploaded document.

---

# 🚀 Core Features

✅ PDF Upload

✅ Intelligent Chunking

✅ Local Embeddings

✅ ChromaDB Integration

✅ Semantic Search

✅ Context-Aware Responses

✅ Prompt Engineering

✅ Local LLM (Llama 3.2)

✅ Source Attribution

✅ Modern Desktop UI

✅ Chat History

✅ Offline AI

✅ Zero API Cost

---

```
```

# 📂 Project Structure

```text
docmind-ai/
│
├── app.py                         # Main Streamlit application
├── config.py                      # Global configuration
├── requirements.txt               # Python dependencies
├── README.md                      # Project documentation
│
├── assets/
│   └── logo.png                   # Application logo
│
├── data/
│   ├── pdfs/                      # Uploaded PDF files
│   └── chroma/                    # ChromaDB persistent storage
│
├── src/
│   │
│   ├── core/
│   │   ├── startup.py
│   │   ├── dependency.py
│   │   └── state.py
│   │
│   ├── ingestion/
│   │   ├── loader.py
│   │   └── chunker.py
│   │
│   ├── embeddings/
│   │   └── embedding_model.py
│   │
│   ├── retrieval/
│   │   ├── retriever.py
│   │   └── vectordb.py
│   │
│   ├── generation/
│   │   ├── llm.py
│   │   └── prompt.py
│   │
│   ├── services/
│   │   └── rag_pipeline.py
│   │
│   ├── ui/
│   │   ├── dashboard.py
│   │   ├── sidebar.py
│   │   ├── chat.py
│   │   ├── styles.py
│   │   └── components/
│   │
│   └── utils/
│       ├── helpers.py
│       ├── metrics.py
│       └── file_manager.py
│
└── venv/
```

---

# 🛠 Technology Stack

| Category | Technology |
|----------|------------|
| Programming Language | Python 3.11+ |
| User Interface | Streamlit |
| AI Framework | LangChain |
| LLM | Llama 3.2 |
| LLM Runtime | Ollama |
| Embedding Model | all-MiniLM-L6-v2 |
| Vector Database | ChromaDB |
| PDF Processing | PyPDF |
| Similarity Search | Cosine Similarity |
| Storage | Local Persistent Storage |

---

# ⚙ Installation

## 1. Clone Repository

```bash
git clone https://github.com/yourusername/docmind-ai.git

cd docmind-ai
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

---

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🤖 Install Ollama

Download Ollama

https://ollama.com

Verify Installation

```bash
ollama --version
```

---

## Pull the LLM

```bash
ollama pull llama3.2
```

You can also use

```bash
ollama pull llama3

ollama pull mistral

ollama pull qwen2.5

ollama pull gemma3
```

Simply update the model name inside

```
src/generation/llm.py
```

---

# ▶ Running the Application

Start the Streamlit server

```bash
streamlit run app.py
```

The application will be available at

```
http://localhost:8501
```

---

# 💡 Using DocMind AI

### Step 1

Launch the application.

---

### Step 2

Upload a PDF document from the sidebar.

---

### Step 3

Click

```
🚀 Process Document
```

The application will

- Read the PDF
- Split into chunks
- Generate embeddings
- Store vectors inside ChromaDB

---

### Step 4

Once indexing is complete,

start chatting with your document.

---

# 💬 Example Questions

```
Summarize this document.

What is Battery Management System?

Explain Chapter 4.

List all important points.

Generate interview questions.

Create revision notes.

Explain this in simple language.

Find information related to thermal management.

What conclusions were drawn?

Give me key takeaways.
```

---

# 🔍 How Semantic Search Works

Traditional keyword search

```
Question

↓

Exact Keyword Match

↓

Few Results
```

---

DocMind AI

```
Question

↓

Embedding

↓

Vector Search

↓

Semantic Similarity

↓

Most Relevant Context

↓

LLM

↓

Accurate Answer
```

Instead of matching words,

the system understands the **meaning** of your question.

---

# 📊 Workflow

```
Upload PDF

↓

Extract Text

↓

Chunk Document

↓

Generate Embeddings

↓

Store in ChromaDB

↓

User Question

↓

Similarity Search

↓

Prompt Builder

↓

Llama 3.2

↓

Answer with Sources
```

---

# 📸 Screenshots

## Home

```
docs/screenshots/home.png
```

---

## Upload Document

```
docs/screenshots/upload.png
```

---

## AI Chat

```
docs/screenshots/chat.png
```

---

## Knowledge Base

```
docs/screenshots/dashboard.png
```

*(Replace these placeholders with actual screenshots after deployment.)*

---
# 🔐 Privacy & Security

One of the biggest advantages of **DocMind AI** is that every component runs **locally** on your machine.

Unlike cloud-based AI platforms, your documents are **never uploaded** to third-party servers.

## Your data stays on your device

- ✅ No OpenAI API
- ✅ No Claude API
- ✅ No Gemini API
- ✅ No Internet required after setup
- ✅ Local Embeddings
- ✅ Local Vector Database
- ✅ Local LLM
- ✅ Complete Data Ownership

This makes DocMind AI suitable for:

- 🏥 Healthcare
- ⚖ Legal Firms
- 🏦 Banking
- 🏢 Enterprises
- 🎓 Universities
- 🔬 Research Organizations
- 📑 Government Departments

---

# ⚡ Performance

DocMind AI is optimized for local execution.

## Current Capabilities

- Fast PDF Processing
- Persistent Vector Database
- Low Latency Responses
- Intelligent Semantic Search
- Context-aware Answers
- Modern Desktop Interface
- Offline AI Inference
- Source Attribution
- Chat History
- Reusable Knowledge Base

---

# 📈 Future Roadmap

The current version is **Version 1.0**.

The following features are planned for future releases.

## Version 1.1

- Multi PDF Chat
- Drag & Drop Upload
- Better UI
- PDF Preview
- Improved Citation Display

---

## Version 2.0

- Folder Indexing
- DOCX Support
- TXT Support
- Markdown Support
- CSV Support
- PowerPoint Support
- OCR for Scanned PDFs

---

## Version 3.0

- Voice Assistant
- Speech to Text
- Text to Speech
- AI Meeting Notes
- Image Understanding
- Vision Models
- AI Agent Support

---

## Enterprise Edition

- Multi-user Authentication
- User Roles
- Team Workspaces
- Knowledge Sharing
- REST API
- Admin Dashboard
- Usage Analytics
- Docker Deployment
- Kubernetes Support
- Cloud Deployment
- API Integrations

---

# 🚀 Deployment

The project can be deployed using:

- Docker
- Ubuntu VPS
- DigitalOcean
- AWS EC2
- Azure Virtual Machine
- Google Cloud Compute Engine
- Local Windows Server

> **Note:** Since DocMind AI relies on **Ollama**, it cannot be deployed directly to static hosting platforms like GitHub Pages, Netlify, or Vercel.

---

# 📊 Development Highlights

### Architecture

- Modular Folder Structure
- Dependency Injection
- Session State Management
- Component-based UI
- Clean Separation of Concerns

### AI Pipeline

- PDF Parsing
- Document Chunking
- Embedding Generation
- Vector Storage
- Similarity Retrieval
- Prompt Engineering
- Local LLM Inference

### User Experience

- Responsive Desktop Interface
- Chat-style Interaction
- Upload Progress
- AI Thinking Indicator
- Response Time Tracking
- Source References

---

# 🧪 Testing

The application has been tested with

- Small PDFs
- Large Research Papers
- Technical Documentation
- User Manuals
- Academic Notes
- Company SOPs
- Legal Documents

---

# 🤝 Contributing

Contributions are always welcome.

If you would like to improve DocMind AI:

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Push your branch.
5. Open a Pull Request.

Example:

```bash
git checkout -b feature/new-feature
git commit -m "Added new feature"
git push origin feature/new-feature
```

---

# 📄 License

This project is licensed under the **MIT License**.

You are free to:

- Use
- Modify
- Distribute
- Commercialize

Please include the original license and copyright notice.

---

# 👨‍💻 Author

## Niyaz Ahmed

**AI Developer | Full Stack Engineer | Founder**

Specializing in:

- Artificial Intelligence
- Retrieval-Augmented Generation (RAG)
- Large Language Models (LLMs)
- LangChain
- Python
- FastAPI
- Next.js
- AI Automation
- Enterprise AI Solutions

---

# 🌟 Support the Project

If you found this project useful,

please consider giving it a ⭐ on GitHub.

It helps others discover the project and supports future development.

```bash
⭐ Star the repository
🍴 Fork the project
📢 Share with others
```

---

# 💼 Need a Custom AI Solution?

I build production-ready AI applications for businesses, including:

- 🤖 Private AI Chatbots
- 📄 AI Document Assistants
- 🧠 Enterprise Knowledge Bases
- 🔍 Semantic Search Systems
- 🏢 Internal AI Tools
- ⚡ Workflow Automation
- 📊 AI Dashboards
- 💬 Customer Support Assistants
- 📚 RAG Applications
- 🚀 End-to-End AI Solutions

If you're looking to integrate AI into your business, feel free to connect.

---

<div align="center">

## ⭐ Built with Python, LangChain, Ollama & Streamlit

### Thanks for visiting the repository!

**Happy Building! 🚀**

</div>
