# # 14. 先頭からN行を出力
# n =int(input('N: '))
# with open('popular-names.txt') as f:
#     for i in range(n):
#         print(f.readline(), end='')

# # head -n 5 popular-names.txt
# # tail -n 5 popular-names.txt

# # 15. 末尾のN行を出力
# n =int(input('N: '))
# with open('popular-names.txt') as f:
#     lines = f.readlines()
#     for line in lines[-n:]:
#         print(line, end='')

# # 16 ファイルをN分割する
# n =int(input('N: '))
# with open('popular-names.txt') as f:
#     lines = f.readlines()
#     unit = -(-len(lines) // n)  # math.ceil(len(lines) / n)の代わり
#     for i in range(n):
#         with open(f'popular-names_{i}.txt', 'w') as f:
#             f.writelines(lines[i*unit:(i+1)*unit])
# split -l 3 popular-names.txt popular-names_
# split -l [行数] [入力ファイル] [出力ファイルの接頭辞]
# -(-len(lines) // n) は切り上げのテクニック

# 17. １列目の文字列の異なり
# 1列目に現れる文字列の「ユニーク（重複なし）な集合」を求める
# unique_words = set()
# # setは集合を表すデータ型で重複を許さない
# with open ('popular-names.txt') as f:
#     for line in f:
#         cols = line.split('\t')
#         unique_words.add(cols[0])

# for word in sorted(unique_words):
#     print(word)
    #sortedでa,b,cの順番に並び替える 
# cut -f1 popular-names.txt | sort | uniq
# cut -f1 popular-names.txt：cutコマンドでファイルの1列目を抽出します（-f1は1列目を意味します）。
# sort：抽出した列をソートします。
# uniq：ソートされた結果からユニークな行のみを表示します。

# 18. 各行を3コラム目の数値の降順にソート
with open('popular-names.txt') as f:
    lines = f.readlines()
    lines.sort(key=lambda line: int(line.split('\t')[2]), reverse=True)

with open('sorted_popular-names.txt', 'w') as f:
    f.writelines(lines)
# lines.sort(key=lambda line: int(line.split('\t')[2]), reverse=True)
# 意味は、各行をタブで分割し、3列目を数値として取得し、それを降順でソートすること

# sort -k 3 -n -r -t$'\t' popular-names.txt
# sort -k 3 -n -r -t$'\t' popular-names.txt > sorted_popular-names.txt
# -k 3：3列目をキーとして指定, -n：数値としてソート, -r：降順でソート -t$'\t'：タブ区切りであることを指定

