import re
import quiz26 as q26

def remove_links():
    d = q26.remove_emphases()
    return {key: re.sub(r'\[\[.*?\|?(.+?)\]\]', '', val) for key, val in d.items()}
# [[]]で囲まれている箇所があったら、その中身を取り出す。ただし、その中に|があったら|の後ろだけを取り出す


if __name__ == "__main__":
    text = remove_links()
    print(text)