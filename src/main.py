from data_processing import standardize_text
from splitter import split
from parser import parse_pdf
from embedding import embedding

def main():
    text = "花椰菜Acknowledged as a common vegetable."
    print(embedding(text))

    path = "docs/pumpkin_book.pdf"
    pages = parse_pdf(path)
    
    print(f'type = {type(pages)} ,len = {len(pages)}')
    page = pages[15]
    text = page.page_content[0:][:300]
    print(f"每一个元素的类型：{type(page)}.", 
        f"该文档的描述性数据：{page.metadata}", 
        f"查看该文档的内容:\n{text}", 
        f"查看format文档：\n{standardize_text(text)}",
        f"查看split文档：\n{split(standardize_text(text))}",
        sep="\n------\n")

if __name__ == "__main__":
    main()