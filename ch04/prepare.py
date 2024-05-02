# 前処理
import MeCab

def prepare():
    mecab = MeCab.Tagger('')
    with open("../neko.txt", "r") as f, open("../neko.txt.mecab", "w") as f2:
        for text in f:
            result = mecab.parse(text)
            f2.write(result)

# 表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音 という形式で形態素解析結果が出力されている

if __name__ == '__main__':
    prepare()
    print('Done')