#46 動詞の格フレーム情報の抽出
# 45のプログラムを改変し，述語と格パターンに続けて項（述語に係っている文節そのもの）をタブ区切り形式で出力せよ．45の仕様に加えて，以下の仕様を満たすようにせよ．

# 項は述語に係っている文節の単語列とする（末尾の助詞を取り除く必要はない）
# 述語に係る文節が複数あるときは，助詞と同一の基準・順序でスペース区切りで並べる

from quiz41 import parse_cabocha

def extract_verb_frames(file_path):
    sentences = parse_cabocha(file_path)
    frames = []
    
    for sentence in sentences:
        for chunk in sentence:
            verbs = [morph.base for morph in chunk.morphs if morph.pos == '動詞']
            if verbs:
                verb = verbs[0]  # 最左の動詞の基本形
                particles = []  # 助詞のリスト
                clauses = []    # 係っている文節のリスト
                
                for src in chunk.srcs:
                    src_chunk = sentence[src]
                    src_particles = [morph.base for morph in src_chunk.morphs if morph.pos == '助詞']
                    if src_particles:
                        # 最後の助詞を使用
                        particles.append(src_particles[-1])
                        # その文節全体を取得
                        clause = ''.join(morph.surface for morph in src_chunk.morphs)
                        clauses.append(clause)
                
                if particles:
                    # 助詞と項を辞書順に並べる
                    pairs = sorted(zip(particles, clauses))
                    sorted_particles = ' '.join(particle for particle, clause in pairs)
                    sorted_clauses = ' '.join(clause for particle, clause in pairs)
                    frames.append(f"{verb}\t{sorted_particles}\t{sorted_clauses}")
    
    return frames

if __name__ == '__main__':
    verb_frames = extract_verb_frames('ai.ja.txt.parsed')
    with open('verb_frames.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(verb_frames))
