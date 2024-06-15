import pandas as pd
from sklearn.model_selection import train_test_split

# データの読み込み
file_path = 'ch06/newsCorpora.csv'  # ファイルのパスを指定
columns = ['ID', 'TITLE', 'URL', 'PUBLISHER', 'CATEGORY', 'STORY', 'HOSTNAME', 'TIMESTAMP']
data = pd.read_csv(file_path, sep='\t', header=None, names=columns)

# 指定された情報源の抽出
publishers = ["Reuters", "Huffington Post", "Businessweek", "Contactmusic.com", "Daily Mail"]
filtered_data = data[data['PUBLISHER'].isin(publishers)]

# データのシャッフルと分割
train_data, temp_data = train_test_split(filtered_data, test_size=0.2, random_state=42)
valid_data, test_data = train_test_split(temp_data, test_size=0.5, random_state=42)

# ファイルへの書き出し（カテゴリ名と記事見出しをタブ区切りで保存）
train_data[['CATEGORY', 'TITLE']].to_csv('ch06/train.txt', sep='\t', index=False, header=False)
valid_data[['CATEGORY', 'TITLE']].to_csv('ch06/valid.txt', sep='\t', index=False, header=False)
test_data[['CATEGORY', 'TITLE']].to_csv('ch06/test.txt', sep='\t', index=False, header=False)

# 各カテゴリの事例数を確認
print("Training data category distribution:")
print(train_data['CATEGORY'].value_counts())
print("\nValidation data category distribution:")
print(valid_data['CATEGORY'].value_counts())
print("\nTest data category distribution:")
print(test_data['CATEGORY'].value_counts())
