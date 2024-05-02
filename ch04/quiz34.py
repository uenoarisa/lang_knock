# 34.名詞の連接
# 名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．
from quiz30 import load_mecab_output

def surface_noun():
    results = load_mecab_output()
    ans = set()
    for morphs in results:
        word = []
        for morph in morphs:
            if morph['pos'] != '名詞':
                if len(word) > 1:
                    ans.add(''.join(word))
                    # word自体は名詞のリストなので、joinで連結することで名詞の連接を取得できる
                word = []
            else:
                word.append(morph['surface'])
        if len(word) > 1:
            ans.add(''.join(word))
    return ans

if __name__ == '__main__':
    noun_set= surface_noun()
    print(noun_set)

