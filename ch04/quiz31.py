# 31. 動詞
# 動詞の表層形をすべて抽出せよ
from quiz30 import load_mecab_output


def surface_base():
    sentences = load_mecab_output()
    suf_list = []
    for sentence in sentences:
        for text in sentence:
            if text["pos"] == "動詞":
                suf_list.append(text["surface"])
    return suf_list

if __name__ == '__main__':
   suf_list = surface_base()
   print(suf_list)

