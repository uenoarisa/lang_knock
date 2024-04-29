import re
import quiz20 as q20

def extract_template():
    text = q20.read_json()
    # 基礎情報の部分を抽出
    base_info = re.search(r'\{\{基礎情報.*?\n\}\}', text, re.DOTALL)
    if base_info:
        base_info = base_info.group()
    else:
        return {}

    # フィールド名と値のペアを抽出
    fields = re.findall(r'\n\|([^=]+?)\s*=\s*(.*?)(?=\n\||\n\}\})', base_info, re.DOTALL)
    # [^=]等号 = 以外の任意の1文字
    # \n\|(.+?)\s=\s(.+?)(?:(?=\n\|)|(?=\}\}\n))これだと無理だった

    # フィールド値の後処理：余分な改行の削除、テキストの整形など
    processed_fields = {field.strip(): value.strip().replace('\n', ' ') for field, value in fields}


    return processed_fields


if __name__ == "__main__":
    text = extract_template()
    print(text)