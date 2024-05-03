# 形態素解析
# 文を形態素（言語で意味を持つ最小単位）に分割し、品詞等を判別する作業
# 係り受け解析
# 各単語間の「主語・述語」「修飾語・被修飾語」などの関係を調べること

# 40. 係り受け解析結果の読み込み（形態素）
# 形態素を表すクラスMorphを実装せよ．このクラスは表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をメンバ変数に持つこととする．さらに，係り受け解析の結果（ai.ja.txt.parsed）を読み込み，各文をMorphオブジェクトのリストとして表現し，冒頭の説明文の形態素列を表示せよ．
# 表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,基本形,読み,発音
# * 係り先の文節番号 係り元の文節番号D 係りの種類 係りのスコア(省略可能)

class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

def parse_morphs(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        sentences = []
        sentence = []
        eos_count = 0

        for line in file:
            if line.strip() == 'EOS':
                eos_count += 1
                if eos_count == 2:  # 2回目のEOSが確認されたら文を保存
                    if sentence:
                        sentences.append(sentence)
                        sentence = []
                    eos_count = 0
                continue
            else:
                eos_count = 0
                if line[0] != '*':
                    parts = line.split('\t')
                    if len(parts) == 2:
                        details = parts[1].split(',')
                        sentence.append(Morph(parts[0], details[6], details[0], details[1]))

    return sentences

if __name__ == '__main__':
    sentences = parse_morphs('../ai.ja.txt.parsed')
    for morph in sentences[1]:  # 説明文(2段落目)の形態素を表示
        print(morph.surface,morph.base,morph.pos,morph.pos1)
