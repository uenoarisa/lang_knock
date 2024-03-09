# 20 JSONデータの読み込み
# Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．
import json

with open('jawiki-country.json', 'r') as f:
    for line in f:
        data = json.loads(line)
        if data['title'] == 'イギリス':
            x = data['text']
            # print(data['text'])
            break

# 21 カテゴリ名を含む行を抽出
import re
# reは正規表現を扱うためのライブラリ
# 正規表現とは、文字列のパターンを記述するための言語
# 正規表現を使うことで、文字列の検索や置換を行うことができる
# for line in x.split("\n"):
    # if re.search(r'\[\[Category:', line):
        # print(line)
# これだと行が表示されない


# re.search(r'\[\[Category:', line)は、lineに[[Category:が含まれているかどうかを調べる
# re.search(正規表現, 検索対象の文字列)
# r とは、raw stringの略で、バックスラッシュをエスケープ文字として扱わない文字列を指す


# 22 カテゴリ名の抽出
# 21の出力結果からカテゴリ名を抽出せよ．
category_lines = re.findall(r'\[\[Category:(.*?)(?:\|.*)?\]\]', x)

# for line in category_lines:
#     print(line)

# 23 セクション構造
# 記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．
import re

# セクション名とそのレベルを抽出して表示
section_pattern = re.compile(r'(==+)(.*?)(==+)')
# .*でどんな文字列でも良いことを示す
# ?で最小限の文字列をマッチさせる
# re.compile()は正規表現をコンパイルする関数
matches = section_pattern.findall(x)
for match in matches:
    # セクション名の前後にある等号の数でレベルを決定
    # print(match[0],match[1])
    # match[0]は==, match[1]はセクション名
    level = len(match[0]) - 1  # 前後の等号は同じ数なので、どちらを数えても良い
    section_name = match[1].strip()  #stripメソッドは、文字列の両端にある特定の文字を取り除くために使われる。何も指定しない場合は、空白文字（スペース、タブ、改行など）を取り除く。
    print(f"セクション名: {section_name}, レベル: {level}")