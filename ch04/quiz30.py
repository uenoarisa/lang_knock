# 30. 形態素解析結果の読み込み
def load_mecab_output():
    results = []
    morphs = []
    with open('../neko.txt.mecab', 'r', encoding='utf-8') as f:
        for row in f:
            if row == 'EOS\n':
                if len(morphs):
                    results.append(morphs)
                    morphs = []
            else:
                cols1 = row.split('\t')
                cols2 = cols1[1].split(',')
                if len(cols2) < 7:
                    continue
                morph = {'surface': cols1[0],
                         'base': cols2[6],
                         'pos': cols2[0],
                         'pos1': cols2[1],
                        }
                morphs.append(morph)
    if len(morphs):
        results.append(morphs)
        morphs = []
    return results


if __name__ == '__main__':
    # 最初の数文の形態素を表示してみる
    sentences=load_mecab_output()
    print(sentences)
