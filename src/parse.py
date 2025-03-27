from langchain_community.document_loaders import PyMuPDFLoader
from langchain_community.document_loaders import UnstructuredMarkdownLoader

def parse_pdf(pdf_path):
    loader = PyMuPDFLoader(pdf_path)
    pdf_pages  = loader.load()
    return pdf_pages 

def parse_md(md_path):
    loader = UnstructuredMarkdownLoader(md_path)
    md_pages = loader.load()
    return md_pages

if __name__ == "__main__":
    path = "docs/Introduction.md"
    pages = parse_md(path)
    
    print(f'type = {type(pages)} ,len = {len(pages)}')
    page = pages[0]
    print(f"每一个元素的类型：{type(page)}.", 
        f"该文档的描述性数据：{page.metadata}", 
        f"查看该文档的内容:\n{page.page_content[0:][:200]}", 
        sep="\n------\n")