# 45
# 今回用いている文章をコーパスと見なし，日本語の述語が取りうる格を調査したい． 動詞を述語，動詞に係っている文節の助詞を格と考え，述語と格をタブ区切り形式で出力せよ
from quiz41 import parse_cabocha

def extract_verb_cases(file_path):
    sentences = parse_cabocha(file_path)
    patterns = []
    
    for sentence in sentences:
        for chunk in sentence:
            verbs = [morph.base for morph in chunk.morphs if morph.pos == '動詞']
            if verbs:
                # 最左の動詞の基本形を取得
                verb = verbs[0]
                cases = []
                
                # この動詞に係る文節の助詞をすべて集める
                for src in chunk.srcs:
                    particles = [morph.base for morph in sentence[src].morphs if morph.pos == '助詞']
                    if particles:
                        # 最後の助詞を採用
                        cases.append(particles[-1])
                
                if cases:
                    cases_sorted = ' '.join(sorted(cases))
                    patterns.append(f"{verb}\t{cases_sorted}")
    
    return patterns

if __name__ == '__main__':
    verb_patterns = extract_verb_cases('ai.ja.txt.parsed')
    with open('verb_patterns.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(verb_patterns))
