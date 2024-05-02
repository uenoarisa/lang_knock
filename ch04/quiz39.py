# 39 Zipfの法則Permalink
# 単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．
from quiz30 import load_mecab_output
from quiz38 import overlap
import matplotlib.pyplot as plt
import japanize_matplotlib
import collections

if __name__ == '__main__':
    data = overlap()
    temp2 = sorted((data.values()), reverse = True)
    plt.plot(temp2)
    plt.xlabel('出現頻度順位')
    plt.ylabel('出現頻度')
    ax = plt.gca()
    # ax(図全体を指すオブジェクト)の指定があればそれを適用し、指定が無ければmatplotlibによって作成する
    ax.set_yscale('log')
    ax.set_xscale('log')
    plt.show()

# zipの法則
# 出現頻度が k 番目に大きい要素が、1位のものの頻度と比較して 1/kに比例する