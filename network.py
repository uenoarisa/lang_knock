from janome.tokenizer import Tokenizer
import re
from itertools import combinations
from collections import Counter
import networkx as nx
import matplotlib.pyplot as plt
import japanize_matplotlib
from matplotlib import font_manager

# Janome: 日本語のテキストをトークン化するために使用。
# NetworkX: ネットワークグラフの作成と操作を行うために使用。
# Matplotlib: ネットワークグラフを含む各種グラフの描画を行うために使用。

# 仮のアンケート回答データ
responses = [
    "会社のコミュニケーションは改善が必要です。",
    "プロジェクト管理ツールが使いづらい。",
    "チームの協力体制は素晴らしい。",
    "もっとフレックスタイムを活用したい。",
    "給与体系についてもっと透明性がほしい。"
]


# 形態素解析器の初期化
t = Tokenizer()

# テキストを単語に分割する関数
def tokenize(text):
    tokens = [token.surface for token in t.tokenize(text) if token.part_of_speech.startswith('名詞')]
    return tokens

# テキストデータの前処理
processed_responses = [tokenize(re.sub(r"[^\w\s]", "", response)) for response in responses]

# 単語のペアの共起をカウント
cooccurrences = Counter()

for response in processed_responses:
    # 同一回答内のすべての単語ペアに対してカウント
    for word_pair in combinations(response, 2):
        cooccurrences[word_pair] += 1

print(cooccurrences)

# ネットワークグラフの初期化
G = nx.Graph()

# 共起関係をグラフに追加
for word_pair, weight in cooccurrences.items():
    G.add_edge(word_pair[0], word_pair[1], weight=weight)


# ネットワークグラフの描画
plt.figure(figsize=(10, 10))
plt.title('アンケート回答の共起ネットワーク')
pos = nx.spring_layout(G, k=0.5) # ノードの位置を決定
nx.draw(G, pos, with_labels=True, font_weight="bold", node_size=2000, node_color="skyblue", font_size=10,font_family='Hiragino Sans')

# エッジラベルの描画
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d['weight'] for u, v, d in G.edges(data=True)})

plt.show()

#


