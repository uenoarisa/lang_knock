# 43. 名詞を含む文節が動詞を含む文節に係るものを抽出
# 名詞を含む文節が，動詞を含む文節に係るとき，これらをタブ区切り形式で抽出せよ．ただし，句読点などの記号は出力しないようにせよ．
from quiz41 import parse_cabocha

def extract_SV(file_path):
    sentences = parse_cabocha(file_path)
    dependencies = [] #名詞を含む文節と動詞を含む文節のペアを保存するためのリスト
    for sentence in sentences:
        for chunk in sentence:
            # 係り先が動詞を含む文節かどうかをチェック
            if chunk.dst != -1 and any(morph.pos == '動詞' for morph in sentence[chunk.dst].morphs):
                # 係り元が名詞を含む文節かどうかをチェック
                if any(morph.pos == '名詞' for morph in chunk.morphs):
                    src_surface = ''.join([morph.surface for morph in chunk.morphs if morph.pos != '記号']) #名詞を含む文節の表層形
                    dst_surface = ''.join([morph.surface for morph in sentence[chunk.dst].morphs if morph.pos != '記号']) #動詞を含む文節の表層形
                    src_surface = src_surface.replace('\t', '')
                    dst_surface = dst_surface.replace('\t', '')
                    dependencies.append((src_surface, dst_surface))
    return dependencies



if __name__ == '__main__':
    dependencies = extract_SV('ai.ja.txt.parsed')
    for src, dst in dependencies:
        print(f'{src}\t{dst}')