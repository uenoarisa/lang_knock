from transformers import pipeline

from transformers import pipeline

classifier = pipeline(
    task="sentiment-analysis",
    model="daigo/bert-base-japanese-sentiment",
    tokenizer="daigo/bert-base-japanese-sentiment"
)

sentence1 = "嬉しいです"
sentence2 = "残念です"
result1 = classifier(sentence1)[0]
result2 = classifier(sentence2)[0]
print(f"label: {result1['label']}, with score: {round(result1['score'], 4)}")
print(f"label: {result2['label']}, with score: {round(result2['score'], 4)}")

# 分析するテキスト
texts = [
    "会社のコミュニケーションは改善が必要です。",
    "プロジェクト管理ツールが使いづらい。",
    "チームの協力体制は素晴らしい。",
    "もっとフレックスタイムを活用したい。",
    "給与体系についてもっと透明性がほしい。"
]