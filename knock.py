# 00.文字列の逆順
x = "stressed"
print("00",x[::-1])
# x[::-1]は、文字列を逆順にするスライス

#01 「パタトクカシーー」
x = "パタトクカシーー"
print("01",x[::2])

# 02.パトカー」＋「タクシー」＝「パタトクカシーー」
x = "パトカー"
y = "タクシー"
print("02","".join([i + j for i, j in zip(x, y)]))

#########################################
# zip(x, y)でxとyの要素を同時に取り出す
# [i + j for i, j in zip(x, y)]でxとyの要素を結合してリストにする
# print([i + j for i, j in zip(x, y)])
#['パタ', 'トク', 'カシ', 'ーー']
##########################################

# 03.円周率
x="Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
# ,と.を削除
x = x.replace(",","").replace(".","")
# 
print("03",[len(i) for i in x.split()])

# 04.元素記号
x="Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
x = x.replace(".","").split()
print("04",{x[i][:1] if i+1 in [1,5,6,7,8,9,15,16,19] else x[i][:2] for i in range(len(x))})

#05. n-gram
# n_gramとは、任意の文字列や文書を連続したn個の文字で分割するテキスト分割方法の一つである。
# 特に、nが1の場合をユニグラム（uni-gram）、2の場合をバイグラム（bi-gram）、3の場合をトライグラム（tri-gram）と呼ぶ。
def n_gram(x, n):
    return [x[i:i+n] for i in range(len(x)-n+1)]

x = "I am an NLPer".split()
y = list("I am an NLPer".replace(" ",""))
print("05 word bi-gram",n_gram(x,2))
print("05 bi-gram",n_gram(y,2))

# 06.集合
x = "paraparaparadise"
y = "paragraph"
X = set(n_gram(x,2))
Y = set(n_gram(y,2))
print("06",X.union(Y))
# 和集合
print("06",X.intersection(Y))
# 積集合
print("06",X.difference(Y))
# 差集合
print("06","se" in X)
print("06","se" in Y)

# 07.テンプレートによる文生成
def template(x,y,z):
    return f"{x}時の{y}は{z}"
x = 12
y = "気温"
z = 22.4
print("07",template(x,y,z))

# 08.暗号文
#暗号化
def cipher(x):
    return "".join([chr(219-ord(i)) if i.islower() else i for i in x])

x = "I am an NLPer"
# chrはASCIIコードを文字に変換、ordは文字をASCIIコードに変換
print("08",cipher(x))
print("08",cipher(cipher(x)))

# 09.Typoglycemia
x = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
x = x.split()
import random
x = [i if len(i) <= 4 else i[0] + "".join(random.sample(i[1:-1], len(i)-2)) + i[-1] for i in x]
print("09"," ".join(x))