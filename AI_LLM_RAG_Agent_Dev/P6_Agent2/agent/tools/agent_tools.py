# 1. Python 标准库
import csv
import os
import random
import threading
from typing import Any, Dict

# 2. 第三方依赖包
from langchain_core.tools import tool

# 3. 业务层内部模块
from rag.rag_service import RagSummarizeService

# 4. 通用工具 utils
from utils.config_handler import agent_conf
from utils.logger_handler import logger
from utils.path_tool import get_abs_path

_get_rag_service = RagSummarizeService()


# 模拟数据：实际场景可由会话/登录态提供
USER_IDS = [
    "1001", "1002", "1003", "1004", "1005",
    "1006", "1007", "1008", "1009", "1010",
]
MONTH_ARR = [
    "2025-01", "2025-02", "2025-03", "2025-04", "2025-05", "2025-06",
    "2025-07", "2025-08", "2025-09", "2025-10", "2025-11", "2025-12",
]

external_data = {}

@tool(description="从向量存储中检索参考资料")
def rag_summarize(query: str) -> str:
    return _get_rag_service.rag_summarize(query)


@tool(description="获取指定城市的天气，以消息字符串的形式返回")
def get_weather(city: str) -> str:
    return f"城市{city}天气为晴天，气温26摄氏度，空气湿度50%，南风1级，AQI21，最近6小时降雨概率极低"


@tool(description="获取用户所在城市的名称，以纯字符串形式返回")
def get_user_location() -> str:
    return random.choice(["深圳", "上海", "杭州"])


@tool(description="获取用户的ID，以纯字符串形式返回")
def get_user_id() -> str:
    return random.choice(USER_IDS)


@tool(description="获取当前月份，以纯字符串形式返回")
def get_current_month() -> str:
    return random.choice(MONTH_ARR)


def generate_external_data():
    """
    模拟生成外部数据，实际场景中可由数据库/接口提供

    {
        "user_id": {
            "month": {
                "specs": "", "efficiency": "XXX", "quality": "", "safety": ""
            },
              "month": {
                "specs": "", "efficiency": "XXX", "quality": "", "safety": ""
            }
            ...
        },
         "user_id": {
            "month": {
                "specs": "", "efficiency": "XXX", "quality": "", "safety": ""
            },
              "month": {
                "specs": "", "efficiency": "XXX", "quality": "", "safety": ""
            }
            ...
        },
        ...
    }
    """
    if not external_data:
        externa_data_path = get_abs_path(agent_conf["external_data_path"])

        if not os.path.exists(externa_data_path):
            raise FileNotFoundError(f"External data file not found: {externa_data_path}")
        
        with open(externa_data_path, "r", encoding="utf-8") as f:
            
            for line in f.readlines()[1:]:
                line = line.strip()
                arr: list[str] = line.strip().split(",")
                user_id = arr[0].replace('"', '')
                feature = arr[1].replace('"', '')
                efficiency = arr[2].replace('"', '')
                consumbles = arr[3].replace('"', '')
                comparison = arr[4].replace('"', '')
                time = arr[5].replace('"', '')

                if user_id not in external_data:
                    external_data[user_id] = {}

                external_data[user_id][time] = {
                    "feature": feature,
                    "efficiency": efficiency,
                    "consumbles": consumbles,
                    "comparison": comparison,
                    "time": time
                }

@tool(description="从外部系统中获取指定用户在指定月份的使用记录，以纯字符串返回，如果未检索到返回空字符串")
def fetch_user_external_data(user_id: str, month: str) -> str:
    generate_external_data()

    try:
        return external_data[user_id][month]
    except KeyError:
        logger.warning(f"No external data found for user_id: {user_id}, month: {month}")
        return ""

@tool(description= "无入参，无返回值，调用后触发中间件自动为报告生成的场景动态注入上下文信息，为后续提示词切换提供上下文信息")
def fill_context_for_report():
    return "fill_context_for_report has been called"
# if __name__ == "__main__":
#     print(fetch_user_external_data("1001", "2025-01"))