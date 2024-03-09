# 10 行数のカウント
# 行数をカウントせよ．確認にはwcコマンドを用いよ．
f = open("popular-names.txt",'r')
print("08",len(f.readlines()))
# wcコマンドとは、ファイルの行数、単語数、文字数をカウントするコマンド  
# wc -l popular-names.txt

# 11.タブをスペースに置換
f = open("popular-names.txt",'r')
print("11",f.read().replace("\t"," "))
# sedコマンドとは、ファイルの中身を置換するコマンド
# sed 's/\t/ /g' popular-names.txt
# trコマンドとは、ファイルの中身を置換するコマンド
# tr '\t' ' ' < popular-names.txt
# タブの表現は\t、スペースの表現は\s
# expandコマンドとは、タブをスペースに変換するコマンド

# 12. 1列目をcol1.txtに，2列目をcol2.txtに保存
# ファイルの読み込み
with open("popular-names.txt", 'r') as f:
    lines = f.readlines()

# 1列目と2列目を保存するためのリストを初期化
col1 = []
col2 = []

# 各行を処理して、1列目と2列目のデータを抽出
for line in lines:
    columns = line.strip().split('\t')  # タブで分割
    # strip:文字列の両端（先頭、末尾）の指定した文字を削除する
    col1.append(columns[0])
    col2.append(columns[1])

# 1列目のデータをcol1.txtに保存
with open("col1.txt", 'w') as f1:
    f1.write('\n'.join(col1))

# 2列目のデータをcol2.txtに保存
with open("col2.txt", 'w') as f2:
    f2.write('\n'.join(col2))

# cutコマンドとは、ファイルの中身を切り取るコマンド
# cut -f 1 popular-names.txt > col1_check.txt
# cut -f 2 popular-names.txt > col2_check.txt
# diffコマンドとは、ファイルの中身を比較するコマンド
# diff col1.txt col1_check.txt
# diff col2.txt col2_check.txt

# 13. col1.txtとcol2.txtをマージ
# col1.txt と col2.txt を読み込む
with open('col1.txt', 'r') as col1_file, open('col2.txt', 'r') as col2_file:
    col1 = col1_file.readlines()
    print('col1',col1)
    col2 = col2_file.readlines()
    print('col2',col2)

# 新しいファイルに結合して書き出す
with open('combined.txt', 'w') as combined_file:
    for line1, line2 in zip(col1, col2):
        combined_file.write(f"{line1.strip()}\t{line2}")

# コマンド
# paste col1.txt col2.txt > combined_check.txt
# diff combined.txt combined_check.txt
# pasteコマンドとは、ファイルを結合するコマンド
