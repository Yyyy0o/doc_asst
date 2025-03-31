from langchain.text_splitter import RecursiveCharacterTextSplitter

# 知识库中单段文本长度
CHUNK_SIZE = 100

# 知识库中相邻文本重合长度
OVERLAP_SIZE = 10

def split(text):
# 使用递归字符文本分割器
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=OVERLAP_SIZE
    )
    return text_splitter.split_text(text)