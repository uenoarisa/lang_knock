import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
from quiz52 import model_train

# モデルを学習
predictor = model_train()

# 記事見出しをベクトル化
titles = [
    "The stock market crashed due to economic uncertainty.",
    "New species of bird discovered in the Amazon rainforest."
]

# Vectorizerを再利用
vectorizer = predictor.vectorizer
features = vectorizer.transform(titles)

# モデルを再利用
model = predictor.model
predictions = model.predict(features)
probabilities = model.predict_proba(features)

# 数値ラベルをカテゴリに変換
inverse_label_mapping = predictor.inverse_label_mapping
predicted_categories = [inverse_label_mapping[pred] for pred in predictions]

# 結果を表示
for title, category, probability in zip(titles, predicted_categories, probabilities):
    print(f"Title: {title}")
    print(f"Predicted Category: {category}")
    print(f"Probabilities: {probability}\n")
