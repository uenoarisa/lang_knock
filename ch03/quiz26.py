import re
import quiz25 as q25

def remove_emphases():
    d = q25.extract_template()
    return {key: re.sub(r'\'{2,5}', '', val) for key, val in d.items()}

# sub(r'\'{2,5}', '', val)は、valの中にある2~5個の'を削除する

if __name__ == "__main__":
    text = remove_emphases()
    print(text)