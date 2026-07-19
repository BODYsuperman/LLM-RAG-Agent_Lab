import sys
from pathlib import Path

# app.py 位于 P6_Agent2/ 目录下，将其加入搜索路径
sys.path.insert(0, str(Path(__file__).parent))

import streamlit as st
from agent.react_agent import ReactAgent

# ========== 页面配置 ==========
st.set_page_config(
    page_title="智能清洁助手",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ========== 自定义样式 ==========
st.markdown("""
<style>
    /* 主区域背景 */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #e8ecf1 100%);
    }
    /* 聊天气泡圆角 */
    [data-testid="stChatMessage"] {
        border-radius: 16px;
        padding: 12px 16px;
        margin-bottom: 8px;
    }
    /* 用户气泡 */
    [data-testid="stChatMessage"][data-testid-avatar-icon="user"] {
        background: #e3f2fd;
    }
    /* 助手气泡 */
    [data-testid="stChatMessage"][data-testid-avatar-icon="assistant"] {
        background: #ffffff;
        box-shadow: 0 1px 3px rgba(0,0,0,0.08);
    }
    /* 输入框 */
    .stChatInput textarea {
        border-radius: 12px !important;
    }
    /* 侧边栏 */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1a237e 0%, #283593 100%);
    }
    [data-testid="stSidebar"] * {
        color: #ffffff !important;
    }
    /* 标题动画 */
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.7; }
    }
    .thinking-dot {
        animation: pulse 1.5s ease-in-out infinite;
    }
</style>
""", unsafe_allow_html=True)

# ========== 侧边栏 ==========
with st.sidebar:
    st.markdown("## 🤖 智能清洁助手")
    st.divider()
    st.markdown("### 💡 你可以问我")
    st.markdown("""
    - 🏠 我的使用报告
    - 🌧️ 今天适合用机器人吗
    - 🔧 扫地机器人故障排除
    - 📖 选购指南与保养建议
    - 📊 使用记录分析
    """)
    st.divider()
    st.caption("基于 ReAct Agent + RAG 构建")
    st.caption("LangGraph · LangChain · ChromaDB")

    # 清空对话按钮
    if st.button("🗑️ 清空对话", use_container_width=True):
        st.session_state["messages"] = []
        st.rerun()

# ========== 主区域 ==========
st.markdown("""
<div style="display:flex; align-items:center; gap:12px; margin-bottom:4px;">
    <span style="font-size:36px;">🤖</span>
    <div>
        <h1 style="margin:0; padding:0; color:#1a237e;">智能清洁助手</h1>
        <p style="margin:0; padding:0; color:#666; font-size:14px;">
            扫地机器人 & 扫拖一体机 · 专业客服 · 报告生成
        </p>
    </div>
</div>
""", unsafe_allow_html=True)
st.divider()

# ========== 会话状态初始化 ==========
if "agent" not in st.session_state:
    with st.spinner("正在初始化 Agent..."):
        st.session_state["agent"] = ReactAgent()

if "messages" not in st.session_state:
    st.session_state["messages"] = []

# ========== 显示历史消息 ==========
for message in st.session_state["messages"]:
    with st.chat_message(message["role"], avatar="🧑" if message["role"] == "user" else "🤖"):
        st.markdown(message["content"])

# ========== 用户输入 ==========
prompt = st.chat_input("请输入您的问题，例如：给我生成使用报告")

if prompt:
    # 显示用户消息
    with st.chat_message("user", avatar="🧑"):
        st.markdown(prompt)
    st.session_state["messages"].append({"role": "user", "content": prompt})

    # 流式输出助手回复
    with st.chat_message("assistant", avatar="🤖"):
        response_chunks = []
        res_stream = st.session_state["agent"].execute_stream(prompt)

        def capture(generator, cache_list):
            for chunk in generator:
                cache_list.append(chunk)
                yield chunk

        st.write_stream(capture(res_stream, response_chunks))

    # 拼接完整回复存入会话
    full_response = "".join(response_chunks)
    st.session_state["messages"].append({"role": "assistant", "content": full_response})
