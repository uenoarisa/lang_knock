# 33. 「AのB」
# 2つの名詞が「の」で連結されている名詞句を抽出せよ．
from quiz30 import load_mecab_output

def surface_noun():
    sentences = load_mecab_output()
    clause_list = []
    for sentence in sentences:
        for i in range(1, len(sentence) - 1): #のから始まることを考慮
            if sentence[i - 1]["pos"] == "名詞" and sentence[i]["surface"] == "の" and sentence[i + 1]["pos"] == "名詞":
                clause_list.append(sentence[i - 1]["surface"] + sentence[i]["surface"] + sentence[i + 1]["surface"])
    return clause_list

if __name__ == '__main__':
    clause_list= surface_noun()
    print(clause_list)

