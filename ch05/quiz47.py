# 47機能動詞構文のマイニング
from quiz41 import parse_cabocha

def extract_sahen_constructions(file_path):
    sentences = parse_cabocha(file_path)
    frames = []

    for sentence in sentences:
        for chunk in sentence:
            verbs = [morph.base for morph in chunk.morphs if morph.pos == '動詞']
            if verbs:
                verb = verbs[0]  # 最左の動詞の基本形を取得
                sahen_wo = None
                
                # サ変接続名詞 + "を" のパターンを探す
                for src in chunk.srcs:
                    src_chunk = sentence[src]
                    morphs = src_chunk.morphs
                    if len(morphs) > 1 and morphs[-1].surface == 'を' and morphs[-1].pos == '助詞':
                        if morphs[-2].pos1 == 'サ変接続':
                            sahen_wo = morphs[-2].base + morphs[-1].surface + verb
                            break
                
                if sahen_wo:
                    particles = []
                    clauses = []
                    
                    for src in chunk.srcs:
                        src_chunk = sentence[src]
                        src_particles = [morph.base for morph in src_chunk.morphs if morph.pos == '助詞']
                        if src_particles:
                            particle = src_particles[-1]
                            particles.append(particle)
                            clause = ''.join(morph.surface for morph in src_chunk.morphs)
                            clauses.append(clause)

                    if particles:
                        pairs = sorted(zip(particles, clauses))
                        sorted_particles = ' '.join(particle for particle, clause in pairs)
                        sorted_clauses = ' '.join(clause for particle, clause in pairs)
                        frames.append(f"{sahen_wo}\t{sorted_particles}\t{sorted_clauses}")

    return frames

if __name__ == '__main__':
    verb_frames = extract_sahen_constructions('ai.ja.txt.parsed')
    with open('sahen_constructions.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(verb_frames))
