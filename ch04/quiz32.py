# 32. 動詞の基本形
# 動詞の基本形をすべて抽出せよ．
from quiz30 import load_mecab_output


def surface_base():
    sentences = load_mecab_output()
    base_list = []
    for sentence in sentences:
        for text in sentence:
            if text["pos"] == "動詞":
                 base_list.append(text["base"])
    return base_list

if __name__ == '__main__':
    base_list= surface_base()
    print(base_list)

