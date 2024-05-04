# 42. 係り元と係り先の文節の表示
# 係り元の文節と係り先の文節のテキストをタブ区切り形式ですべて抽出せよ．ただし，句読点などの記号は出力しないようにせよ．
from quiz41 import parse_cabocha


if __name__ == '__main__':
    sentences = parse_cabocha('../ai.ja.txt.parsed')
    for sentence in sentences:
        for chunk in sentence:
            # 文節の文字列を作成
            chunk_surface = ''.join([morph.surface for morph in chunk.morphs])
            
            # 係り先の表示
            dst_surface = ''.join([morph.surface for morph in sentence[chunk.dst].morphs]) if chunk.dst != -1 else 'None'
            
            print(f'文節: {chunk_surface}  係り先: {dst_surface}')
        print('-----------------------------')
