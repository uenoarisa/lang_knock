# 20 JSONデータの読み込み
# Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．
import json

def read_json():
    with open('../jawiki-country.json', 'r') as f:
        for line in f:
            data = json.loads(line)
            if data['title'] == 'イギリス':
                x = data['text']
                return x
            
if __name__ == "__main__":
    text = read_json()
    print(text)