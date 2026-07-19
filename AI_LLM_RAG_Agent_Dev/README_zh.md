<div align="center">

# 🤖 AI_LLM_RAG_Agent_Dev

### 从 API 调用到 ReAct Agent —— 一站式 LLM 应用开发实战工程

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://python.org)
[![LangChain](https://img.shields.io/badge/LangChain-1.2-green.svg)](https://github.com/langchain-ai/langchain)
[![LangGraph](https://img.shields.io/badge/LangGraph-1.2-orange.svg)](https://github.com/langchain-ai/langgraph)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.59-red.svg)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**6 大阶段 · 38+ 实战案例 · 渐进式从零构建企业级 AI Agent**

[🚀 快速开始](#-快速开始) · [📖 项目结构](#-项目结构) · [🎯 核心亮点](#-核心亮点) · [📸 效果展示](#-效果展示)

**[English](README.md)** | **中文**

</div>

---

## ✨ 项目简介

本项目是一套 **完整的 LLM 应用开发学习路线**，从最基础的 OpenAI API 调用，到 Prompt 工程优化，再到 LangChain + RAG 知识库检索，最终构建具备 **ReAct 思考能力、动态提示词切换、中间件日志监控** 的企业级智能客服 Agent。

以**扫地机器人智能客服**为业务场景，全流程可运行、可调试、可扩展。

---

## 🎯 核心亮点

| 特性 | 说明 |
|:---|:---|
| 🧠 **ReAct Agent** | 基于 LangGraph 的思考→行动→观察循环，自主决策工具调用 |
| 📚 **RAG 知识库** | ChromaDB + Ollama Embeddings，支持 PDF/TXT 增量入库与 MD5 去重 |
| 🔄 **动态提示词切换** | `fill_context_for_report` 标记工具 + `pre_model_hook` 检测，自动切换报告/客服提示词 |
| 🕵️ **中间件监控** | `pre_model_hook` / `post_model_hook` 全链路日志，记录工具调用参数与 LLM 回复 |
| 📊 **流式报告生成** | 识别用户意图后自动切换为报告写手模式，生成 Markdown 格式的专业分析报告 |
| 💬 **Streamlit 对话界面** | 渐变侧边栏、自定义气泡、流式打字机输出，开箱即用 |
| 📈 **渐进式学习** | P0→P6 六大阶段，每个阶段独立可运行，由浅入深 |

---

## 📖 项目结构

```
AI_LLM_RAG_Agent_Dev/
│
├── 📁 P0_Prequisite/          # 🔧 环境准备 & Ollama 本地模型部署指南
│
├── 📁 P1_OpenAI_Basic_Usage/  # 📡 LLM API 基础调用
│   ├── 01_test_api.py             # API 连通性测试
│   ├── 02_openai_basic_use.py     # 基础对话补全
│   └── 01_agent.py                # 手写最简 Agent（无框架）
│
├── 📁 P2_Prompt_Optimization/ # ✍️ Prompt 工程实战
│   ├── 03_openai_streamout.py             # 流式输出
│   ├── 04_openai_historychatcontent.py    # 多轮对话上下文管理
│   ├── 05_financial_text_classification.py  # 文本分类
│   ├── 06_Json_usage_demo.py              # JSON 结构化输出
│   └── 07_information_extraction_fewshot.py # Few-Shot 信息抽取
│
├── 📁 P3_LangChain_RAG_Dev/   # ⛓️ LangChain 全链路 + RAG
│   ├── 10~12   # 向量相似度 & 模型调用基础
│   ├── 13~15   # Chat Model / Message / Embeddings
│   ├── 16~20   # PromptTemplate / FewShot / Chain 调用
│   ├── 21~25   # Chain 操作符重载 / Runnable / OutputParser
│   ├── 26~27   # 临时会话记忆 & 持久化记忆
│   ├── 28~31   # 文档加载器 (CSV/JSON/Txt/PDF)
│   └── 32~34   # VectorStore → RAG 完整工作流
│
├── 📁 P4_Rag-Clothing-Customer-Service/  # 👗 RAG 实战：服装客服系统
│   ├── app_qa.py               # Streamlit 问答界面
│   ├── app_file_uploader.py    # 知识库文件上传
│   ├── rag.py                  # RAG 检索链
│   └── vector_stores.py        # 向量库管理
│
├── 📁 P5_Agent/               # 🤖 Agent 入门
│   ├── 35_LangChain_Agent_First_Experience.py  # Agent 首体验
│   ├── 36_LangChain_Agent_Stream_Output.py     # Agent 流式输出
│   ├── 37_LangChain_Agent_ReAct_Framework.py   # ReAct 框架
│   └── 38_LangChain_Agent_Middleware.py         # Agent 中间件
│
└── 📁 P6_Agent2/              # 🏆 终极项目：企业级 ReAct Agent
    ├── app.py                  # Streamlit 对话界面
    ├── agent/
    │   ├── react_agent.py          # ReAct Agent 核心（LangGraph）
    │   └── tools/
    │       ├── agent_tools.py      # 7 个业务工具
    │       └── middleware.py       # 日志监控 + 提示词切换钩子
    ├── model/
    │   └── factory.py             # Chat Model & Embedding 工厂
    ├── rag/
    │   ├── vector_store.py        # 向量库服务（ChromaDB）
    │   └── rag_service.py         # RAG 检索摘要链
    ├── prompts/                   # 提示词模板
    │   ├── main_prompt.txt        # 客服主提示词
    │   ├── report_prompt.txt      # 报告生成提示词
    │   └── rag_summarize.txt      # RAG 摘要提示词
    ├── config/                    # YAML 配置中心
    ├── data/                      # 知识库源文件
    └── logs/                      # 运行日志
```

---

## 🏗️ P6 架构图

```
                    ┌──────────────┐
                    │   Streamlit  │  用户交互界面
                    │    app.py    │
                    └──────┬───────┘
                           │ query
                           ▼
                    ┌──────────────┐
                    │  ReactAgent  │  ReAct Agent 核心
                    │ react_agent  │
                    └──────┬───────┘
                           │
              ┌────────────┼────────────────┐
              ▼            ▼                ▼
     ┌─────────────┐ ┌──────────┐  ┌──────────────────┐
     │ pre_model   │ │ LLM 模型 │  │ post_model      │
     │   _hook     │ │ (GLM-5)  │  │   _hook         │
     │             │ │          │  │                  │
     │ • 日志记录   │ │ 思考→决策 │  │ • 回复日志       │
     │ • 提示词切换 │ │ 工具调用  │  │ • 工具结果记录    │
     └──────┬──────┘ └────┬─────┘  └──────────────────┘
            │              │
            ▼              ▼
     ┌─────────────────────────────────────────┐
     │              7 个业务工具                  │
     ├─────────────┬────────────┬───────────────┤
     │ rag_summarize│ get_weather│ get_user_id   │
     │ (RAG检索)    │ (天气查询)  │ (用户ID)      │
     ├─────────────┼────────────┼───────────────┤
     │ get_location │ get_month  │ fetch_external│
     │ (用户城市)    │ (当前月份)  │ (使用记录)     │
     ├─────────────┼────────────┴───────────────┤
     │ fill_context_for_report                   │
     │ (报告意图标记 → 触发提示词切换)              │
     └───────────────────────────────────────────┘
            │
            ▼
     ┌─────────────────────────────────────────┐
     │              RAG 知识库                    │
     │  ChromaDB + Ollama Embeddings            │
     │  选购指南 / 100问 / 故障排除 / 维护保养      │
     └─────────────────────────────────────────┘
```

---

## 🔄 提示词切换流程

这是本项目最核心的设计模式 —— **意图标记 + 钩子检测 + 动态切换**：

```
用户: "给我生成使用报告"
         │
         ▼
  LLM 调用 get_user_id → get_current_month → fill_context_for_report
         │
         ▼
  pre_model_hook 检测到 ToolMessage(name="fill_context_for_report")
         │
         ▼
  返回 {"llm_input_messages": [SystemMessage(report_prompt)] + messages}
  ┌─ state.messages 不变 ─┐  ┌─ LLM 看到的提示词换了 ─┐
  │  仍为原始对话记录       │  │  从"客服模式"→"报告写手"  │
  └────────────────────────┘  └─────────────────────────┘
         │
         ▼
  LLM 用 report_prompt 调用 fetch_user_external_data
         │
         ▼
  生成 Markdown 格式的专业分析报告
```

---

## 🚀 快速开始

### 1. 环境准备

```bash
# 克隆项目
git clone https://github.com/yourname/Ai_LLM_RAG_Agent_Dev.git
cd Ai_LLM_RAG_Agent_Dev

# 创建虚拟环境
python3 -m venv .venv
source .venv/bin/activate

# 安装依赖
pip install -r P6_Agent2/requirements.txt
```

### 2. 配置模型

编辑 `P6_Agent2/config/rag.yml`，填入你的 API Key（或使用本地 Ollama）：

```yaml
chat_model_name: glm-5            # 智谱 GLM / OpenAI 兼容模型
embedding_model_name: qwen3-embedding  # Ollama 本地 Embedding
```

确保 Ollama 已运行并拉取 Embedding 模型：

```bash
ollama pull qwen3-embedding
```

### 3. 运行终极项目

```bash
cd P6_Agent2

# 命令行模式
python3 agent/react_agent.py

# Web 对话界面
streamlit run app.py
```

### 4. 运行各阶段示例

```bash
# P1: API 基础
python3 P1_OpenAI_Basic_Usage/01_test_api.py

# P2: Prompt 工程
python3 P2_Prompt_Optimization/05_financial_text_classification.py

# P3: LangChain RAG
python3 P3_LangChain_RAG_Dev/33_LangChain_RAG_Complete_Workflow.py

# P4: RAG 服装客服
streamlit run P4_Rag-Clothing-Customer-Service/app_qa.py

# P5: Agent 入门
python3 P5_Agent/37_LangChain_Agent_ReAct_Framework.py
```

---

## 📸 效果展示

### 🤖 智能客服对话

> **用户**: 今天适合用扫地机器人吗？
>
> **Agent**: 让我先获取您的城市和天气信息...
> → 调用 `get_user_location` → 深圳
> → 调用 `get_weather` → 晴天，26℃，湿度50%，AQI 21
> → 基于天气环境给出使用建议 ✅

### 📊 报告自动生成

> **用户**: 给我生成我的使用报告
>
> **Agent**:
> 1. 自动获取用户 ID、月份
> 2. 调用 `fill_context_for_report` 触发提示词切换
> 3. 检索使用记录数据
> 4. 生成 Markdown 格式的专业分析报告 📋

### 📝 全链路日志

```log
[pre_model_hook] 消息数量: 4
[pre_model_hook] 检测到 fill_context_for_report 已调用 → 切换为报告提示词
[post_model_hook] LLM 选择调用工具: fetch_user_external_data | 参数: {'user_id': '1005', 'month': '2025-06'}
[post_model_hook] 工具 fetch_user_external_data 返回结果: {"feature": "120㎡ | 老人 | 防滑砖"...}
```

---

## 🛠️ 技术栈

| 层级 | 技术 |
|:---|:---|
| **LLM** | 智谱 GLM-5 / OpenAI 兼容 API |
| **Embedding** | Ollama + Qwen3-Embedding（本地） |
| **Agent 框架** | LangGraph（ReAct） |
| **RAG 链** | LangChain Core（PromptTemplate → LLM → StrOutputParser） |
| **向量库** | ChromaDB |
| **文档加载** | PyPDF / TextLoader（LangChain Community） |
| **文本切分** | RecursiveCharacterTextSplitter |
| **前端** | Streamlit |
| **配置** | YAML 多模块配置中心 |
| **日志** | Python logging + TimedRotatingFileHandler |

---

## 📚 学习路线

```
P0 环境准备 → P1 API调用 → P2 Prompt工程 → P3 LangChain+RAG → P4 RAG实战 → P5 Agent入门 → P6 企业级Agent
   📦           📡             ✍️              ⛓️                👗            🤖              🏆
  Ollama      OpenAI       流式/分类/抽取    完整RAG链        服装客服       ReAct框架      动态提示词+中间件
```

每个阶段都是前一阶段的延伸，可独立运行，也可按顺序学习。

---

## 🤝 贡献

欢迎 Issue 和 PR！如果你有新的工具、提示词策略或 Agent 模式想要添加，非常欢迎。

---

## 📄 License

[MIT License](LICENSE)

---

<div align="center">

**如果这个项目对你有帮助，给个 ⭐ Star 吧！**

Made with 🧠 + ❤️

</div>
