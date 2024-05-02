# 37「猫」と共起頻度の高い上位10語
# 「猫」とよく共起する（共起頻度が高い）10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．
from quiz30 import load_mecab_output
import matplotlib.pyplot as plt
import japanize_matplotlib
from collections import defaultdict

def co_occurrence():
    results = load_mecab_output()
    cooc_dict = defaultdict(int)
    for sentence in results:
        # 文中に「猫」が存在するかチェック
        if any(morph['surface'] == '猫' for morph in sentence):
            # 「猫」を除いたその他の単語の頻度を数える
            for morph in sentence:
                if morph['surface'] != '猫':
                    cooc_dict[morph['surface']] += 1

    # 頻度が高い順に10個の単語を取得
    cooc_list = sorted(cooc_dict.items(), key=lambda x: x[1], reverse=True)[:10]
    return cooc_list

if __name__ == '__main__':
    co_occurrence_list = co_occurrence()
    words, counts = zip(*co_occurrence_list)  # アンパックしてリストを2つのリストに分ける
    plt.figure(figsize=(10, 5))
    plt.bar(words, counts)
    plt.title('「猫」と共起頻度が高い上位10語')
    plt.xlabel('単語')
    plt.ylabel('共起頻度')
    plt.show()
