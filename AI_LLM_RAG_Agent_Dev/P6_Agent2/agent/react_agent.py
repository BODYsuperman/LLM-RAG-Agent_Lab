# import sys
# from pathlib import Path

# # 当前文件：P6_Agent2/agent/react_agent.py
# # 往上两级 = AI_LLM_RAG_Agent_Dev 项目根目录
# root_path = Path(__file__).parent.parent.parent
# sys.path.append(str(root_path))


# # 标准库/第三方导入
# from langgraph.prebuilt import create_react_agent
# from model.factory import chat_model
# from utils.prompt_loader import load_system_prompts

# # 业务工具导入，括号多行消除末尾逗号报错
# from agent.tools.agent_tools import (
#     rag_summarize,
#     get_weather,
#     get_user_location,
#     get_user_id,
#     get_current_month,
#     fetch_user_external_data,
#     fill_context_for_report,
# )
# from agent.tools.middleware import log_and_switch_prompt, log_after_model


# class ReactAgent:
#     # 删掉无用的 agent 形参，内部自己构建agent
#     def __init__(self):
#         self.tools = [
#             rag_summarize,
#             get_weather,
#             get_user_location,
#             get_user_id,
#             get_current_month,
#             fetch_user_external_data,
#             fill_context_for_report
#         ]
#         self.middleware = [monitor_tool, log_before_model, report_prompt_switch]
#         self.system_prompt = load_system_prompts()
#         self.model = chat_model

#         # # 按langchain标准调整create_agent入参，根据实际框架修正
#         # self.agent = create_agent(
#         #     llm=self.model,
#         #     tools=self.tools,
#         #     prompt=self.system_prompt,
#         #     middleware=self.middleware
#         # )

#         self.agent = create_agent(
#             llm=self.model,
#             tools=self.tools,
#             prompt=self.system_prompt,
#             middleware=self.middleware
#         )

#     # 增加 query 入参，接收外部提问
#     def execute_stream(self, query: str):
#         input_dict = {
#             "message": [
#                 {
#                     "role": "user",
#                     "content": query
#                 }
#             ]
#         }
#         # 修正stream传参语法，全部放入括号内
#         stream_gen = self.agent.stream(
#             input_dict,
#             stream_mode="values",
#             context={"report": False}
#         )
#         for chunk in stream_gen:
#             messages = chunk.get("message", [])
#             if not messages:
#                 continue
#             latest_message = messages[-1]
#             # 仅输出非空内容
#             content = latest_message.content.strip()
#             if content:
#                 yield content + "\n"


# if __name__ == "__main__":
#     # 实例化不再传参
#     react_agent = ReactAgent()
#     query_text = "请帮我分析用户1001在2025-01月份的使用记录，并结合外部数据和天气数据给出建议"
#     # 传入query
#     for response in react_agent.execute_stream(query_text):
#         print(response, end="", flush=True)

import sys
from pathlib import Path

# 精准计算项目根目录并插入到搜索路径最前面
file_path = Path(__file__)
# react_agent.py → agent → P6_Agent2
project_root = file_path.parent.parent
sys.path.insert(0, str(project_root))

# 第三方导入
from langgraph.prebuilt import create_react_agent

# 项目内部模块
from model.factory import chat_model
from utils.prompt_loader import load_system_prompts

from agent.tools.agent_tools import (
    rag_summarize,
    get_weather,
    get_user_location,
    get_user_id,
    get_current_month,
    fetch_user_external_data,
    fill_context_for_report,
)
from agent.tools.middleware import log_and_switch_prompt, log_after_model


class ReactAgent:
    def __init__(self):
        self.tools = [
            rag_summarize,
            get_weather,
            get_user_location,
            get_user_id,
            get_current_month,
            fetch_user_external_data,
            fill_context_for_report
        ]
        self.system_prompt = load_system_prompts()
        self.llm = chat_model

        self.agent = create_react_agent(
            model=self.llm,
            tools=self.tools,
            prompt=self.system_prompt,
            pre_model_hook=log_and_switch_prompt,
            post_model_hook=log_after_model
        )

    def execute_stream(self, query: str):
        input_dict = {
            "messages": [
                {
                    "role": "user",
                    "content": query
                }
            ]
        }
        stream_gen = self.agent.stream(
            input_dict,
            stream_mode="values"
        )

        for chunk in stream_gen:
            messages = chunk.get("messages", [])
            if not messages:
                continue
            latest_message = messages[-1]
            content = latest_message.content.strip()
            if content:
                yield content + "\n"


if __name__ == "__main__":
    react_agent = ReactAgent()
    query_text = "给我生成我的使用报告"
    for response in react_agent.execute_stream(query_text):
        print(response, end="", flush=True)