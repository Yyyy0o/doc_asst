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