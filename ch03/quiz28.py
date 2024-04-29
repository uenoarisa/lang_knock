import re
import quiz27 as q27

def remove_markups():
    d = q27.remove_links()
    d = {key: re.sub(r'\[http:.+?\s(.+?)\]', '', val) for key, val in d.items()}
    # ref（開始タグも終了タグもまとめて）とbrを除去
    d = {key: re.sub(r'</?(ref|br).*?>', '', val) for key, val in d.items()}
    # テンプレートの除去 ({{テンプレート名|パラメータ1|パラメータ2}} -> 空文字)
    d = {key: re.sub(r'\{\{[^}]+\}\}', '', val) for key, val in d.items()}
    return d



if __name__ == "__main__":
    text = remove_markups()
    print(text)