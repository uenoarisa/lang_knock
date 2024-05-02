# 35 単語の出現頻度
# 文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．
from quiz30 import load_mecab_output

def word_count():
    results = load_mecab_output()
    ans = {}
    for morphs in results:
        for morph in morphs:
            # 単語なので、補助記号、助詞、助動詞は除外
            if morph["pos"] != "補助記号" and morph["pos"] != "助詞" and morph["pos"] != "助動詞":
                if morph['surface'] in ans:
                    ans[morph['surface']] += 1
                else:
                    ans[morph['surface']] = 1
    ans = sorted(ans.items(), key=lambda x: x[1], reverse=True)
    return ans

if __name__ == '__main__':
    word_count= word_count()
    print(word_count[:10])

