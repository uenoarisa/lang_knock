import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

# データの読み込み
train_df = pd.read_csv('ch06/train.txt', sep='\t', header=None, names=['CATEGORY', 'TITLE'])
valid_df = pd.read_csv('ch06/valid.txt', sep='\t', header=None, names=['CATEGORY', 'TITLE'])
test_df = pd.read_csv('ch06/test.txt', sep='\t', header=None, names=['CATEGORY', 'TITLE'])

# ベクトル化のための準備（特徴量の数を制限）
vectorizer = CountVectorizer(max_features=1000)

# 訓練データの見出しから特徴量を抽出
X_train = vectorizer.fit_transform(train_df['TITLE'])
# fit_transformメソッドは、以下の2つの操作をする
# fit: テキストデータから語彙（ボキャブラリー）を学習。
# transform: 学習した語彙を使ってテキストデータを数値ベクトルに変換
train_features = pd.DataFrame(X_train.toarray(), columns=vectorizer.get_feature_names_out())

# 検証データの見出しから特徴量を抽出
X_valid = vectorizer.transform(valid_df['TITLE'])
valid_features = pd.DataFrame(X_valid.toarray(), columns=vectorizer.get_feature_names_out())

# 評価データの見出しから特徴量を抽出
X_test = vectorizer.transform(test_df['TITLE'])
test_features = pd.DataFrame(X_test.toarray(), columns=vectorizer.get_feature_names_out())

# ファイルに保存
train_features.to_csv('ch06/train.feature.txt', index=False)
valid_features.to_csv('ch06/valid.feature.txt', index=False)
test_features.to_csv('ch06/test.feature.txt', index=False)

print("特徴量の抽出と保存が完了しました。")
