# 23 セクション構造
# 記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．
import re
import quiz20 as q20

x = q20.read_json()
# セクション名とそのレベルを抽出して表示
section_pattern = re.compile(r'(==+)(.*?)(==+)')
# .*でどんな文字列でも良いことを示す
# ?で最小限の文字列をマッチさせる
# re.compile()は正規表現をコンパイルする関数
matches = section_pattern.findall(x)

def extract_section_structure():
    for match in matches:
        # セクション名の前後にある等号の数でレベルを決定
        # print(match[0],match[1])
        # match[0]は==, match[1]はセクション名
        level = len(match[0]) - 1  # 前後の等号は同じ数なので、どちらを数えても良い
        section_name = match[1].strip()  #stripメソッドは、文字列の両端にある特定の文字を取り除くために使われる。何も指定しない場合は、空白文字（スペース、タブ、改行など）を取り除く。
        print (f"{section_name}, レベル{level}")
    

if __name__ == "__main__":
    text = extract_section_structure()