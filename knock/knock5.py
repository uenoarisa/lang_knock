import json

with open('jawiki-country.json', 'r') as f:
    for line in f:
        data = json.loads(line)
        if data['title'] == 'イギリス':
            x = data['text']
            # print(data['text'])
            break

# 24 ファイル参照の抽出
# 記事から参照されているメディアファイルをすべて抜き出せ．
# メディアファイルの正規表現
import re
media_file_pattern = re.compile(r'\[\[ファイル:(.*?)\|')

for line in x.split("\n"):
    match = media_file_pattern.search(line)
    if match:
        # print(match)
        # <re.Match object; span=(8, 60), match='[[ファイル:Royal Coat of Arms of the United Kingdom.s>これが出力される
        print(match.group(1))
        # group(1)は1番目の()で囲まれた部分を取得する
        # Royal Coat of Arms of the United Kingdom.svg
        # group(0)は、正規表現全体にマッチした文字列全体を取得するために使われる。つまり、[[ファイル:Royal Coat of Arms of the United Kingdom.svg|...のような全体のマッチ文字列を返す。
        # group(1)は、最初のキャプチャグループにマッチした部分、この場合はRoyal Coat of Arms of the United Kingdom.svgのような[[ファイル:と最初の|の間にある文字列を取得するために使われる。


