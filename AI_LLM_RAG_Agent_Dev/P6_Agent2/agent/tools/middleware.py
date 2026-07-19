from typing import Any, Dict

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage, ToolMessage

from utils.logger_handler import logger
from utils.prompt_loader import load_system_prompts, load_report_prompts

# 缓存提示词，避免每次调用都读文件
_system_prompt = load_system_prompts()
_report_prompt = load_report_prompts()


def _is_report_mode(messages: list) -> bool:
    """检查消息列表中是否有 fill_context_for_report 的 ToolMessage，判断是否进入报告模式。"""
    for msg in messages:
        if isinstance(msg, ToolMessage) and msg.name == "fill_context_for_report":
            return True
    return False


def log_and_switch_prompt(state: Dict[str, Any]) -> Dict[str, Any]:
    """
    pre_model_hook: 记录消息状态 + 根据是否调用过 fill_context_for_report 切换提示词。
    返回 llm_input_messages 会覆盖 LLM 实际收到的消息（不影响 state 中的 messages）。
    """
    messages = state.get("messages", [])
    logger.info(f"[pre_model_hook] 消息数量: {len(messages)}")

    if messages:
        last_msg = messages[-1]
        msg_type = type(last_msg).__name__
        content_preview = last_msg.content[:200] if hasattr(last_msg, 'content') and last_msg.content else ""
        logger.info(f"[pre_model_hook] 最新消息类型: {msg_type} | 内容摘要: {content_preview}")

        if isinstance(last_msg, AIMessage) and last_msg.tool_calls:
            for tc in last_msg.tool_calls:
                logger.info(f"[pre_model_hook] AI 请求调用工具: {tc['name']} | 参数: {tc['args']}")

    # 检查是否需要切换到报告提示词
    is_report = _is_report_mode(messages)
    prompt_text = _report_prompt if is_report else _system_prompt

    if is_report:
        logger.info("[pre_model_hook] 检测到 fill_context_for_report 已调用 → 切换为报告提示词")

    # 构建 LLM 输入消息：SystemMessage(提示词) + 原有消息
    llm_input_messages = [SystemMessage(content=prompt_text)] + messages

    # 返回 llm_input_messages：只影响 LLM 看到的内容，不修改 state 的 messages
    return {"llm_input_messages": llm_input_messages}


def log_after_model(state: Dict[str, Any]) -> Dict[str, Any]:
    """
    post_model_hook: 每次 LLM 调用后执行，记录 LLM 的回复。
    """
    messages = state.get("messages", [])
    if messages:
        last_msg = messages[-1]
        msg_type = type(last_msg).__name__
        logger.info(f"[post_model_hook] LLM 回复类型: {msg_type}")

        if isinstance(last_msg, AIMessage):
            if last_msg.content:
                content_preview = last_msg.content[:200]
                logger.info(f"[post_model_hook] LLM 回复内容: {content_preview}")
            if last_msg.tool_calls:
                for tc in last_msg.tool_calls:
                    logger.info(f"[post_model_hook] LLM 选择调用工具: {tc['name']} | 参数: {tc['args']}")

    # 记录工具执行结果（ToolMessage）
    tool_messages = [m for m in messages if isinstance(m, ToolMessage)]
    for tm in tool_messages[-3:]:
        content_preview = str(tm.content)[:200]
        logger.info(f"[post_model_hook] 工具 {tm.name} 返回结果: {content_preview}")

    return {}
