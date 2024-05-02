# 38ヒストグラム
# 単語の出現頻度のヒストグラムを描け．ただし，横軸は出現頻度を表し，1から単語の出現頻度の最大値までの線形目盛とする．縦軸はx軸で示される出現頻度となった単語の異なり数（種類数）である．
from quiz30 import load_mecab_output
import matplotlib.pyplot as plt
import japanize_matplotlib
import collections

def overlap():
    general_list = load_mecab_output()
    word_list = []
    for sentense in general_list:
        for text in sentense:
            word_list.append(text["surface"]) #単語のリストを作成
    data = collections.Counter(word_list) #単語の出現頻度をカウント
    return data


if __name__ == '__main__':
    data = overlap()
    plt.hist(data.values(), range(1, 30)) #30はグラフへの描画数
    plt.xlabel('出現頻度')
    plt.ylabel('単語の異なり数')
    plt.show()
