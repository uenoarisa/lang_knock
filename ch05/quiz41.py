# 41. 係り受け解析結果の読み込み（文節・係り受け）
# 40に加えて，文節を表すクラスChunkを実装せよ．このクラスは形態素（Morphオブジェクト）のリスト（morphs），係り先文節インデックス番号（dst），係り元文節インデックス番号のリスト（srcs）をメンバ変数に持つこととする．さらに，入力テキストの係り受け解析結果を読み込み，１文をChunkオブジェクトのリストとして表現し，冒頭の説明文の文節の文字列と係り先を表示せよ．本章の残りの問題では，ここで作ったプログラムを活用せよ．

from quiz40 import Morph

class Chunk:
    def __init__(self, dst):
        self.morphs = []         # 形態素（Morphオブジェクト）のリスト
        self.dst = dst           # 係り先文節インデックス番号
        self.srcs = []           # 係り元文節インデックス番号のリスト

def parse_cabocha(file_path):
    sentences = []
    chunks = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if line.startswith('*'):
                cols = line.split()
                idx = int(cols[1])
                dst = int(cols[2].rstrip('D'))
                if idx not in chunks:
                    chunks[idx] = Chunk(dst)
                else:
                    chunks[idx].dst = dst
                if dst != -1:
                    if dst not in chunks:
                        chunks[dst] = Chunk(None)
                    chunks[dst].srcs.append(idx)
            elif line.strip() == 'EOS':
                if chunks:
                    sentences.append(list(chunks.values()))
                    chunks = {}
            else:
                parts = line.split('\t')
                if len(parts) == 2:
                    surface, details = parts
                    base, pos, pos1 = details.split(',')[6], details.split(',')[0], details.split(',')[1]
                    chunks[idx].morphs.append(Morph(surface, base, pos, pos1))
    return sentences

if __name__ == '__main__':
    sentences = parse_cabocha('../ai.ja.txt.parsed')
    for chunk in sentences[1]:
        # 文節の形態素（Morphオブジェクト）のリストを表示
        print("形態素（Morphオブジェクト）のリスト:")
        for morph in chunk.morphs:
            print(f"表層形：{morph.surface} / 基本形：{morph.base} / 品詞：{morph.pos} / 品詞細分類1：{morph.pos1}")
        
        # 係り先文節インデックス番号を表示
        print(f"係り先文節インデックス番号：{chunk.dst}")
        
        # 係り元文節インデックス番号のリストを表示
        print(f"係り元文節インデックス番号のリスト：{chunk.srcs}")
        
        print("-----------------------------")
    print('=============================')
        