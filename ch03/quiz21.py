# 21. カテゴリ名を含む行を抽出Permalink
# 記事中でカテゴリ名を宣言している行を抽出せよ．

import re
from quiz20 import read_json

def extract_category_lines():
    x = read_json()
    return re.findall(r'.*\[\[Category.*', x)

if __name__ == "__main__":
    text = extract_category_lines()
    print(text)

# カテゴリ名を抽出
# *Category.*の詳細
# *は直前の文字が0回以上繰り返すことを示す
# .は改行を除く任意の1文字
# だから行を抽出することができる