import chromadb
from chromadb.config import Settings

# 初始化 Chroma 客户端
client = chromadb.Client(Settings(
    chroma_db_impl="duckdb+parquet",
    persist_directory=".chromadb"
))

def save_documents(self, documents):
    """
    保存文档到 Chroma 向量库
    :param documents: 文档列表
    """
    # 生成文档的嵌入向量
    embeddings = self.embedding_model.encode(documents).tolist()
    # 生成唯一的 ID 列表
    ids = [str(i) for i in range(len(documents))]
    # 向集合中添加文档及其嵌入向量
    self.collection.add(
        embeddings=embeddings,
        documents=documents,
        ids=ids
    )

def retrieve_documents(self, query, n_results=3):
    """
    根据查询检索相关文档
    :param query: 查询文本
    :param n_results: 返回的结果数量
    :return: 相关文档列表
    """
    # 生成查询的嵌入向量
    query_embedding = self.embedding_model.encode(query).tolist()
    # 从集合中查询相关文档
    results = self.collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )
    # 返回查询结果中的文档列表
    # 检查结果是否为空
    if results and 'documents' in results and results['documents']:
        return results['documents'][0]
    return []
