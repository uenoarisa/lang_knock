# 22. カテゴリ名の抽出Permalink
# 記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．
import re
import quiz20 as q20

def extract_category_names():
    x = q20.read_json()
    return re.findall(r'.*Category:(.*?)\]', x)
    # Category:」の直後から最初の]までの間の任意の文字列を取得

if __name__ == "__main__":
    text = extract_category_names()
    print(text)