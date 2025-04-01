from data_processing import standardize_text
from splitter import split
from parser import parse_pdf
import os

def main():
    docs_dir = "docs"
    for root, dirs, files in os.walk(docs_dir):
        for file in files:
            file_path = os.path.join(root, file)
            # 根据文件类型选择不同的处理方法
            if file.endswith('.pdf'):
                documents = parse_pdf(file_path)
                # 标准化文本
                standardized_docs = standardize_text(documents)
                # 分割文本
                chunks = split(standardized_docs)
                # 生成向量嵌入
                for chunk in chunks:
                    print(chunk)
            # 可以添加其他文件类型的处理逻辑
            print(f"Processing file: {file_path}")

if __name__ == "__main__":
    main()