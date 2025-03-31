import re

def standardize_text(text):
    pattern = re.compile(r'[^\u4e00-\u9fff](\n)[^\u4e00-\u9fff]', re.DOTALL)
    return re.sub(pattern,lambda match: match.group(0).replace('\n', ''), text)
