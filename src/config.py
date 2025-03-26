import os
from dotenv import load_dotenv

# 加载.env文件
load_dotenv()

class Config:
    """配置类"""
    API_KEY = os.getenv("API_KEY")
    API_BASE = os.getenv("API_BASE")
    EMBEDING_MODEL = os.getenv("MODEL_ID")
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"
    VERSION = "0.1.0"
    APP_NAME = "doc_asst"