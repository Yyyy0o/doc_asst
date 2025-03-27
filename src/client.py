from volcenginesdkarkruntime import Ark
import os
from config import Config

# 创建OpenAI客户端实例
client = Ark(
    api_key=Config.API_KEY,
    base_url=Config.API_BASE,
)

# 导出client对象供其他模块使用
__all__ = ['client']
