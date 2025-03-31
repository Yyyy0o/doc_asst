from client import client
from config import Config

def embedding(text: str,model=Config.EMBEDING_MODEL) -> list:
    try:
        response = client.embeddings.create(
            model=model,
            input=[text],
            encoding_format="float"
        )
        return response.data[0].embedding
    except Exception as e:
        print(f"获取embedding失败: {str(e)}")
        return []
    