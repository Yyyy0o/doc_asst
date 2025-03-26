from client import client
from config import Config

def get_embedding(text: str) -> list:
    try:
        response = client.embeddings.create(
            model=Config.EMBEDING_MODEL,
            input=[text],
            encoding_format="float"
        )
        return response.data[0].embedding
    except Exception as e:
        print(f"获取embedding失败: {str(e)}")
        return []


if __name__ == "__main__":
    text = "花椰菜Acknowledged as a common vegetable."
    embedding = get_embedding(text)
    print(embedding)