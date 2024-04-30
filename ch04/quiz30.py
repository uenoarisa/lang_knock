# 前処理
import MeCab
import unidic
mecab = MeCab.Tagger()
with open("../neko.txt", "r") as f, open("../neko.txt.mecab", "w") as f2:
    lines = f.readlines()
    for text in lines:
        result = mecab.parse(text)
        f2.write(result)

# 30. 形態素解析結果の読み込み
