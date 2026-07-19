<div align="center">

# 🤖 AI_LLM_RAG_Agent_Dev

### From API Calls to ReAct Agent — A One-Stop LLM Application Development Project

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://python.org)
[![LangChain](https://img.shields.io/badge/LangChain-1.2-green.svg)](https://github.com/langchain-ai/langchain)
[![LangGraph](https://img.shields.io/badge/LangGraph-1.2-orange.svg)](https://github.com/langchain-ai/langgraph)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.59-red.svg)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**6 Stages · 38+ Hands-On Examples · Progressively Build an Enterprise-Grade AI Agent from Scratch**

[🚀 Quick Start](#-quick-start) · [📖 Project Structure](#-project-structure) · [🎯 Key Features](#-key-features) · [📸 Demo](#-demo)

**English** | **[中文](AI_LLM_RAG_Agent_Dev/README_zh.md)**

</div>

---

## ✨ About

This project is a **complete LLM application development learning path** — from basic OpenAI API calls, through Prompt engineering optimization, to LangChain + RAG knowledge retrieval, and finally building an enterprise-grade smart customer service Agent with **ReAct reasoning, dynamic prompt switching, and middleware logging**.

The business scenario is a **smart robot vacuum customer service**, with every stage fully runnable, debuggable, and extensible.

---

## 🎯 Key Features

| Feature | Description |
|:---|:---|
| 🧠 **ReAct Agent** | LangGraph-based Think → Act → Observe loop with autonomous tool-call decision-making |
| 📚 **RAG Knowledge Base** | ChromaDB + Ollama Embeddings with PDF/TXT incremental ingestion and MD5 deduplication |
| 🔄 **Dynamic Prompt Switching** | `fill_context_for_report` marker tool + `pre_model_hook` detection for automatic report/assistant prompt switching |
| 🕵️ **Middleware Monitoring** | `pre_model_hook` / `post_model_hook` full-pipeline logging of tool-call parameters and LLM responses |
| 📊 **Streaming Report Generation** | Automatically switches to report-writer mode upon intent detection, producing Markdown-formatted analysis reports |
| 💬 **Streamlit Chat UI** | Gradient sidebar, custom chat bubbles, streaming typewriter output — ready to use out of the box |
| 📈 **Progressive Learning** | P0→P6 six stages, each independently runnable, building from basics to advanced |

---

## 📖 Project Structure

```
AI_LLM_RAG_Agent_Dev/
│
├── 📁 P0_Prequisite/          # 🔧 Environment Setup & Ollama Local Model Guide
│
├── 📁 P1_OpenAI_Basic_Usage/  # 📡 LLM API Fundamentals
│   ├── 01_test_api.py             # API connectivity test
│   ├── 02_openai_basic_use.py     # Basic chat completion
│   └── 01_agent.py                # Minimal hand-coded Agent (no framework)
│
├── 📁 P2_Prompt_Optimization/ # ✍️ Prompt Engineering in Practice
│   ├── 03_openai_streamout.py             # Streaming output
│   ├── 04_openai_historychatcontent.py    # Multi-turn context management
│   ├── 05_financial_text_classification.py  # Text classification
│   ├── 06_Json_usage_demo.py              # JSON structured output
│   └── 07_information_extraction_fewshot.py # Few-Shot information extraction
│
├── 📁 P3_LangChain_RAG_Dev/   # ⛓️ LangChain Full Pipeline + RAG
│   ├── 10~12   # Cosine similarity & model basics
│   ├── 13~15   # Chat Model / Message / Embeddings
│   ├── 16~20   # PromptTemplate / FewShot / Chain invocation
│   ├── 21~25   # Chain operator overloading / Runnable / OutputParser
│   ├── 26~27   # Temporary & permanent session memory
│   ├── 28~31   # Document loaders (CSV/JSON/Txt/PDF)
│   └── 32~34   # VectorStore → RAG complete workflow
│
├── 📁 P4_Rag-Clothing-Customer-Service/  # 👗 RAG in Action: Clothing Customer Service
│   ├── app_qa.py               # Streamlit Q&A interface
│   ├── app_file_uploader.py    # Knowledge base file upload
│   ├── rag.py                  # RAG retrieval chain
│   └── vector_stores.py        # Vector store management
│
├── 📁 P5_Agent/               # 🤖 Agent Fundamentals
│   ├── 35_LangChain_Agent_First_Experience.py  # First Agent experience
│   ├── 36_LangChain_Agent_Stream_Output.py     # Agent streaming output
│   ├── 37_LangChain_Agent_ReAct_Framework.py   # ReAct framework
│   └── 38_LangChain_Agent_Middleware.py         # Agent middleware
│
└── 📁 P6_Agent2/              # 🏆 Capstone: Enterprise ReAct Agent
    ├── app.py                  # Streamlit chat interface
    ├── agent/
    │   ├── react_agent.py          # ReAct Agent core (LangGraph)
    │   └── tools/
    │       ├── agent_tools.py      # 7 business tools
    │       └── middleware.py       # Logging + prompt-switching hooks
    ├── model/
    │   └── factory.py             # Chat Model & Embedding factory
    ├── rag/
    │   ├── vector_store.py        # Vector store service (ChromaDB)
    │   └── rag_service.py         # RAG retrieval-summary chain
    ├── prompts/                   # Prompt templates
    │   ├── main_prompt.txt        # Main assistant prompt
    │   ├── report_prompt.txt      # Report generation prompt
    │   └── rag_summarize.txt      # RAG summary prompt
    ├── config/                    # YAML config center
    ├── data/                      # Knowledge base source files
    └── logs/                      # Runtime logs
```

---

## 🏗️ P6 Architecture

```
                    ┌──────────────┐
                    │   Streamlit  │  User Interface
                    │    app.py    │
                    └──────┬───────┘
                           │ query
                           ▼
                    ┌──────────────┐
                    │  ReactAgent  │  ReAct Agent Core
                    │ react_agent  │
                    └──────┬───────┘
                           │
              ┌────────────┼────────────────┐
              ▼            ▼                ▼
     ┌─────────────┐ ┌──────────┐  ┌──────────────────┐
     │ pre_model   │ │ LLM Model│  │ post_model      │
     │   _hook     │ │ (GLM-5)  │  │   _hook         │
     │             │ │          │  │                  │
     │ • Logging   │ │ Think →  │  │ • Response log  │
     │ • Prompt    │ │ Decide → │  │ • Tool result   │
     │   switching │ │ Act      │  │   recording     │
     └──────┬──────┘ └────┬─────┘  └──────────────────┘
            │              │
            ▼              ▼
     ┌─────────────────────────────────────────┐
     │              7 Business Tools             │
     ├─────────────┬────────────┬───────────────┤
     │ rag_summarize│ get_weather│ get_user_id   │
     │ (RAG Search) │ (Weather)  │ (User ID)     │
     ├─────────────┼────────────┼───────────────┤
     │ get_location │ get_month  │ fetch_external│
     │ (User City)  │ (Month)    │ (Usage Data)  │
     ├─────────────┼────────────┴───────────────┤
     │ fill_context_for_report                   │
     │ (Report intent marker → trigger prompt    │
     │  switch)                                  │
     └───────────────────────────────────────────┘
            │
            ▼
     ┌─────────────────────────────────────────┐
     │           RAG Knowledge Base              │
     │  ChromaDB + Ollama Embeddings            │
     │  Buying Guide / FAQ / Troubleshooting /  │
     │  Maintenance                             │
     └─────────────────────────────────────────┘
```

---

## 🔄 Dynamic Prompt Switching

The core design pattern of this project — **Intent Marker + Hook Detection + Dynamic Switch**:

```
User: "Generate my usage report"
         │
         ▼
  LLM calls get_user_id → get_current_month → fill_context_for_report
         │
         ▼
  pre_model_hook detects ToolMessage(name="fill_context_for_report")
         │
         ▼
  Returns {"llm_input_messages": [SystemMessage(report_prompt)] + messages}
  ┌─ state.messages unchanged ──┐  ┌─ LLM sees a different prompt ─┐
  │  Original conversation stays │  │  "Assistant" → "Report Writer" │
  └─────────────────────────────┘  └────────────────────────────────┘
         │
         ▼
  LLM uses report_prompt to call fetch_user_external_data
         │
         ▼
  Generates Markdown-formatted professional analysis report
```

---

## 🚀 Quick Start

### 1. Setup

```bash
# Clone the project
git clone https://github.com/yourname/AI_LLM_RAG_Agent_Dev.git
cd Ai_LLM_RAG_Agent_Dev

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r P6_Agent2/requirements.txt
```

### 2. Configure Models

Edit `P6_Agent2/config/rag.yml` with your API key (or use local Ollama):

```yaml
chat_model_name: glm-5            # Zhipu GLM / OpenAI-compatible model
embedding_model_name: qwen3-embedding  # Ollama local Embedding
```

Make sure Ollama is running and the Embedding model is pulled:

```bash
ollama pull qwen3-embedding
```

### 3. Run the Capstone Project

```bash
cd P6_Agent2

# CLI mode
python3 agent/react_agent.py

# Web chat interface
streamlit run app.py
```

### 4. Run Examples from Each Stage

```bash
# P1: API Fundamentals
python3 P1_OpenAI_Basic_Usage/01_test_api.py

# P2: Prompt Engineering
python3 P2_Prompt_Optimization/05_financial_text_classification.py

# P3: LangChain RAG
python3 P3_LangChain_RAG_Dev/33_LangChain_RAG_Complete_Workflow.py

# P4: RAG Clothing Customer Service
streamlit run P4_Rag-Clothing-Customer-Service/app_qa.py

# P5: Agent Fundamentals
python3 P5_Agent/37_LangChain_Agent_ReAct_Framework.py
```

---

## 📸 Demo

### 🤖 Smart Customer Service Chat

> **User**: Is today a good day to use the robot vacuum?
>
> **Agent**: Let me check your city and weather first...
> → Calls `get_user_location` → Shenzhen
> → Calls `get_weather` → Sunny, 26°C, Humidity 50%, AQI 21
> → Provides usage advice based on weather conditions ✅

### 📊 Automated Report Generation

> **User**: Generate my usage report
>
> **Agent**:
> 1. Automatically retrieves user ID and current month
> 2. Calls `fill_context_for_report` to trigger prompt switching
> 3. Fetches usage record data
> 4. Generates a Markdown-formatted professional analysis report 📋

### 📝 Full-Pipeline Logging

```log
[pre_model_hook] Message count: 4
[pre_model_hook] fill_context_for_report detected → switching to report prompt
[post_model_hook] LLM selected tool: fetch_user_external_data | args: {'user_id': '1005', 'month': '2025-06'}
[post_model_hook] Tool fetch_user_external_data returned: {"feature": "120㎡ | Elderly | Anti-slip tiles"...}
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|:---|:---|
| **LLM** | Zhipu GLM-5 / OpenAI-compatible API |
| **Embedding** | Ollama + Qwen3-Embedding (local) |
| **Agent Framework** | LangGraph (ReAct) |
| **RAG Chain** | LangChain Core (PromptTemplate → LLM → StrOutputParser) |
| **Vector Store** | ChromaDB |
| **Document Loading** | PyPDF / TextLoader (LangChain Community) |
| **Text Splitting** | RecursiveCharacterTextSplitter |
| **Frontend** | Streamlit |
| **Configuration** | YAML multi-module config center |
| **Logging** | Python logging + TimedRotatingFileHandler |

---

## 📚 Learning Path

```
P0 Setup → P1 API Calls → P2 Prompt Engineering → P3 LangChain+RAG → P4 RAG Practice → P5 Agent Intro → P6 Enterprise Agent
   📦          📡                 ✍️                    ⛓️                  👗                🤖                   🏆
  Ollama     OpenAI        Streaming/Classify/Extract  Full RAG Chain   Clothing CSR     ReAct Framework    Dynamic Prompts+Middleware
```

Each stage builds on the previous one, can be run independently, or followed sequentially.

---

## 🤝 Contributing

Issues and PRs are welcome! If you have new tools, prompt strategies, or Agent patterns to add, feel free to contribute.

---

## 📄 License

[MIT License](LICENSE)

---

<div align="center">

**If this project helps you, please give it a ⭐ Star!**

Made with 🧠 + ❤️

</div>
