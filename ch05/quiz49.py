from itertools import combinations
from quiz41 import parse_cabocha

def format_chunk(sentence, index, is_noun_replaced, replacement):
    chunk_text = ""
    replaced = False
    for morph in sentence[index].morphs:
        if morph.pos != "記号":
            if morph.pos == "名詞" and not replaced and is_noun_replaced:
                chunk_text += replacement
                replaced = True  # 置換後はフラグを立ててこれ以上置換しない
            else:
                chunk_text += morph.surface
    return chunk_text

def extract_noun_pairs(file_path):
    sentences = parse_cabocha(file_path)
    for sentence in sentences:
        nouns = [i for i, chunk in enumerate(sentence) if any(morph.pos == '名詞' for morph in chunk.morphs)]

        for i, j in combinations(nouns, 2):
            path_I = []
            path_J = []
            seen_i = set()
            seen_j = set()

            while i != j and i not in seen_i and j not in seen_j:
                seen_i.add(i)
                seen_j.add(j)
                if i < j:
                    path_I.append(i)
                    i = sentence[i].dst
                else:
                    path_J.append(j)
                    j = sentence[j].dst

            path_I.append(i)  # 最終的な共通点または目的地を追加
            path_J.append(j)  # 最終的な共通点または目的地を追加

            if i == j:
                formatted_path = ' -> '.join([format_chunk(sentence, idx, idx == path_I[0], 'X') for idx in path_I] +
                                             [format_chunk(sentence, idx, idx == path_J[0], 'Y') for idx in reversed(path_J[:-1])])
                print(formatted_path)
            else:
                # 循環やその他の問題により、合流点が異なる場合
                path_X = ' -> '.join(format_chunk(sentence, idx, idx == path_I[0], 'X') for idx in path_I)
                path_Y = ' -> '.join(format_chunk(sentence, idx, idx == path_J[0], 'Y') for idx in reversed(path_J))
                common = format_chunk(sentence, i, False, '')
                print(f"{path_X} | {path_Y} | {common}")

if __name__ == '__main__':
    extract_noun_pairs('ai.ja.txt.parsed')
