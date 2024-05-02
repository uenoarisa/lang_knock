# 36. 頻度上位10語
# 出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．
from quiz35 import word_count
import matplotlib.pyplot as plt
import japanize_matplotlib
import collections

word_counts= word_count()[:10]
word_list = []
height_list = []
for word in word_counts:
    word_list.append(word[0])
    height_list.append(word[1])

plt.bar(x = word_list ,height = height_list)
plt.title('出現頻度が高い10語')
plt.xlabel('単語')
plt.ylabel('出現頻度')
plt.show()