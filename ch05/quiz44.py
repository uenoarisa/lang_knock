# 44. 係り受け木の可視化
# 与えられた文の係り受け木を有向グラフとして可視化せよ．可視化には，Graphviz等を用いるとよい．

import graphviz
from quiz41 import parse_cabocha

def visualize_dependency(file_path, sentence_index):
    sentences = parse_cabocha(file_path)
    sentence = sentences[sentence_index]
    
    dot = graphviz.Digraph(format='png')
    
    for i, chunk in enumerate(sentence):
        src_surface = ''.join(morph.surface for morph in chunk.morphs if morph.pos != '記号')
        node_label = f"{i}: {src_surface}"
        dot.node(str(i), node_label)
        
        if chunk.dst != -1:
            dst_surface = ''.join(morph.surface for morph in sentence[chunk.dst].morphs if morph.pos != '記号')
            dst_label = f"{chunk.dst}: {dst_surface}"
            dot.edge(str(i), str(chunk.dst), label="依存")
    
    print(dot.source)
    dot.render('dependency_graph', view=True)

if __name__ == '__main__':
    visualize_dependency('ai.ja.txt.parsed',1)
