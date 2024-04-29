import re
import quiz20 as q20

def extract_media_files():
    x = q20.read_json()
    return re.findall(r'(?:ファイル):(.+?)\|', x)

# キャプチャグループ(...)
# 非キャプチャグループ: (?:...)

if __name__ == "__main__":
    text = extract_media_files()
    print(text)