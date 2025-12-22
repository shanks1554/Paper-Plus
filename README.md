# 📚 Paper Plus  
AI-powered research assistant for paper improvement, suggestion, and scientific Q&A.  

Paper Plus is a full-stack application combining Retrieval-Augmented Generation, domain-aware vector search, and research-grade NLP models to improve academic writing, recommend relevant papers, and answer research questions using real scientific context.  

---

## 🚀 Features  

### 🔹 1. Research Paper Improver  
Paste scientific text → get:  
* Academic-style analysis  
* Error detection  
* Structural and reasoning review  
* Optional rewritten output  

### 🔹 2. Research Paper Suggestion System  
Enter a research query → get:  
* Ranked paper suggestions  
* Multi-domain search  
* Score-based ordering  
* Powered by FAISS + LLM reranking  

## Domains include:  

* Artificial Intelligence
* Business
* Medical
* Psychology
* Automobile
* Climate
* Cyber Security
---

### 🔹 3. Research Q&A with RAG  
Ask scientific questions → get:  
* Evidence-based answers  
* Real PDF-sourced context  
* Source document citations  
* Retrieval transparency  

---

## 🏗️ System Architecture  

### 🧠 Backend: FastAPI  
Provides 3 APIs:  

| Endpoint | Purpose |
|---------|---------|
| `/improver/analyze` | Analyze + rewrite text |
| `/suggestion/suggest-papers` | Retrieve + rank papers |
| `/qa/ask` | RAG-based scientific Q&A |

### 💡 RAG + Vector DB  
* FAISS per-domain indexes  
* Chunk-based PDF retrieval  
* LLM scoring + aggregation  
* Multi-domain routing  

### 🖥 Frontend: Flask  
* Three feature pages  
* Web dashboard  
* Clean, modern UI  
* Light theme  

### Pages:  

* Home
* Improver
* Suggestion
* Q&A (Question & Answer)

---
## 🧰 Core Technologies  

**Backend** 
* FastAPI  
* LangChain  
* FAISS  
* Hugging Face LLM  
* Python 3.12  

**Frontend**  
* Flask  
* HTML / CSS / Jinja2  

**Models**  
* `meta-llama/Meta-Llama-3-8B-Instruct`  

---

## 🗂 Project Structure  

```bash
Paper Plus
├── RAG_system/ ← Vector DB + Retrieval + QA
├── research_paper_suggestion_system/
├── research_paper_improver_system/
├── api/ ← FastAPI routes + schemas
├── frontend/ ← Flask + Templates + CSS
├── data/ ← Research PDFs per domain
├── indexes/ ← FAISS + metadata per domain
└── requirements.txt
```
---

## ⚙️ Setup Instructions 

### 1️⃣ Clone the repo  
```bash
git clone <repo-url>
cd Paper-Plus
```
### 2️⃣ Create a .env in root directory with following content:

```bash
HF_TOKEN = Your Hugging Face API Key
```

### 3️⃣ Create a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate # Linux / Mac
.venv\Scripts\activate # Windows
```

### 4️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 5️⃣ Run FastAPI backend
```bash
uvicorn api.main:app --reload
```
Docs available at:
```bash
http://127.0.0.1:8000/docs
```

### 6️⃣ Run Flask frontend

```bash
python frontend/app.py
```
Visit:
```bash
http://127.0.0.1:5000
```
---
## 📊 Data Requirements

Store research PDFs in:
```bash
/data/<domain-name>/
```
Domains must match exactly.

Indexes must exist in:
```bash
/indexes/<domain-name>/
```
---
## 🧪 Testing Guide

| Page       | Test Action         | Expected Result              |
| ---------- | ------------------- | ---------------------------- |
| Improver   | Paste academic text | Analysis + rewritten version |
| Suggestion | Query + domains     | Ranked papers + scores       |
| Q&A        | Question + domain   | Answer + sources             |

---
## 🌟 Future Enhancements

* Multi-domain ranking weights
* PDF viewer integration
* User history saving
* Graph-based source visualization
* Multi-step conversational RAG
---

## 🧑‍💻 Author

Developed by Deep Nagpal

---

## 🏁 Final Notes
Paper Plus is built to scale:
* modular RAG pipelines
* independent vector DBs
* API-first architecture
* reusable LLM interfaces

This system can be deployed, extended, and productized with very little modification.
---
