import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer

class ChromaDocumentTool:
    def __init__(self, collection_name="documents"):
        # 初始化 Chroma 客户端
        self.client = chromadb.Client(Settings(
            chroma_db_impl="duckdb+parquet",
            persist_directory=".chromadb"
        ))
        # 创建或获取集合
        self.collection = self.client.get_or_create_collection(name=collection_name)
        # 初始化句子嵌入模型
        self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

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
        # 持久化保存
        self.client.persist()

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
        return results['documents'][0]