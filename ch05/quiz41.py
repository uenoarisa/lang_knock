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
    chunks = {} #現在の文の文節を保持する辞書。
    eos_count = 0
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
                # 文節が既存でない場合、新しいChunkオブジェクトを作成。既に存在する場合、dstを更新。
                if dst != -1:
                    if dst not in chunks:
                        chunks[dst] = Chunk(None)
                    chunks[dst].srcs.append(idx)

            elif line.strip() == 'EOS':
                eos_count += 1
                if eos_count == 2:  # 2回目のEOSが確認されたら文を保存
                    if chunks:
                        sentences.append(list(chunks.values()))
                        chunks = {}
                    eos_count = 0
                continue
                
            else:
                parts = line.split('\t')
                if len(parts) == 2:
                    surface, details = parts
                    base, pos, pos1 = details.split(',')[6], details.split(',')[0], details.split(',')[1]
                    chunks[idx].morphs.append(Morph(surface, base, pos, pos1))
    return sentences

if __name__ == '__main__':
    sentences = parse_cabocha('ai.ja.txt.parsed')
    for i, chunk in enumerate(sentences[1]):  # sentences[0]で最初の文のデータを表示
        # 現在の文節のテキストを取得（記号を除く）
        current_chunk_text = ''.join(morph.surface for morph in chunk.morphs if morph.pos != '記号')
        
        # 係り先文節のテキストを取得
        if chunk.dst != -1:  # 係り先が存在する場合
            dst_chunk_text = ''.join(morph.surface for morph in sentences[1][chunk.dst].morphs if morph.pos != '記号')
            print(f"文節 {i}: {current_chunk_text} -> 係り先文節 {chunk.dst}: {dst_chunk_text}")
        else:
            print(f"文節 {i}: {current_chunk_text} -> 係り先文節: なし")
        
        print("-----------------------------")


        