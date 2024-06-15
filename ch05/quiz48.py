# 48
# 名詞から根へのパスの抽出
def parse_text(filepath):
    with open(filepath, "r") as f:
        lines = f.readlines()

    dic_list = []
    text_dic = {}
    text = ""
    Flag_N = 0
    Flag_lastline = 0
    index_num = 0
    num = 0

    for line in lines:
        if line == "EOS\n":
            if Flag_lastline == 1:
                if Flag_N == 1:
                    text = "N:" + text
                    Flag_N = 0
                text_dic[index_num] = [text, num]
                dic_list.append(text_dic)
                text_dic = {}
                Flag_lastline = 0
            continue

        if line[0] == "*":
            if Flag_N == 1:
                text = "N:" + text
                Flag_N = 0
            if int(line.split(" ")[1]) != 0:
                text_dic[index_num] = [text, num]
            num = int(line.split(" ")[2][:-1])  # かかり先
            index_num = int(line.split(" ")[1])  # かかり元
            text = ""
            if num == -1:
                Flag_lastline = 1
            continue

        if line.split("\t")[1][0:2] == "記号":
            continue
        text += line.split("\t")[0]
        if line.split("\t")[1].split(",")[0] == "名詞":
            Flag_N = 1

    return dic_list

def build_trees(dic_list):
    result = []
    for sentence in dic_list:
        for key, value in sentence.items():
            if value[0].startswith("N:"):
                temp = ""
                num = key
                while num != -1:
                    word = sentence[num][0].replace("N:", "")
                    temp += word
                    num = sentence[num][1]
                    if num != -1:
                        temp += " -> "
                result.append(temp)
    return result

def extract_noun_paths(filepath):
    dic_list = parse_text(filepath)
    result_list = build_trees(dic_list)
    return result_list

if __name__ == "__main__":
    file_path = 'ai.ja.txt.parsed'
    results = extract_noun_paths(file_path)
    for result in results:
        print(result)
