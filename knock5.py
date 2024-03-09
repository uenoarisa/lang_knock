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