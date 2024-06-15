# 42. 係り元と係り先の文節の表示
# 係り元の文節と係り先の文節のテキストをタブ区切り形式ですべて抽出せよ．ただし，句読点などの記号は出力しないようにせよ．
from quiz41 import parse_cabocha

def extract_dependency(file_path):
    sentences = parse_cabocha(file_path)
    dependencies = []
    for sentence in sentences:
        for chunk in sentence:
            src_surface = ''.join([morph.surface for morph in chunk.morphs if morph.pos != '記号'])
            dst_surface = ''.join([morph.surface for morph in sentence[chunk.dst].morphs if morph.pos != '記号']) if chunk.dst != -1 else 'None'
            src_surface = src_surface.replace('\t', '')
            dst_surface = dst_surface.replace('\t', '')
            dependencies.append((src_surface, dst_surface))
    return dependencies

if __name__ == '__main__':
    dependencies = extract_dependency('ai.ja.txt.parsed')
    for src, dst in dependencies:
        print(f'{src}\t{dst}')