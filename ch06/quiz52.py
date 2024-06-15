import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer

class NewsCategoryPredictor:
    def __init__(self):
        # ロジスティック回帰モデルとテキストベクトル化器を初期化
        self.model = LogisticRegression(max_iter=1000)
        self.vectorizer = CountVectorizer(max_features=1000)
        self.label_mapping = None
        self.inverse_label_mapping = None
        # self.model: ロジスティック回帰モデルを初期化します。
        # self.vectorizer: CountVectorizerを初期化し、最大1000個の特徴量に制限します。
        # self.label_mapping: カテゴリを数値にマッピングする辞書。
        # self.inverse_label_mapping: 数値からカテゴリにマッピングする辞書

    def load_data(self, label_file):
        labels_df = pd.read_csv(label_file, sep='\t', header=None, names=['CATEGORY', 'TITLE'])
        labels = labels_df['CATEGORY'].map(self.label_mapping)
        features = self.vectorizer.transform(labels_df['TITLE'])
        return features, labels

    def train(self, train_label_file):
        # ラベルを数値に変換
        train_labels_df = pd.read_csv(train_label_file, sep='\t', header=None, names=['CATEGORY', 'TITLE'])
        self.label_mapping = {label: idx for idx, label in enumerate(train_labels_df['CATEGORY'].unique())} #カテゴリを数値にマッピングする辞書を作成
        self.inverse_label_mapping = {idx: label for label, idx in self.label_mapping.items()} #数値からカテゴリにマッピングする辞書を作成
        
        # Vectorizerを学習
        self.vectorizer.fit(train_labels_df['TITLE']) #Vectorizerを訓練データのタイトルで学習
        
        train_features, train_labels = self.load_data(train_label_file) #訓練データをベクトル化し、ラベルを数値に変換
        
        # モデルの学習
        self.model.fit(train_features, train_labels)

def model_train():
    # モデルのインスタンス化
    predictor = NewsCategoryPredictor()
    # データの読み込みと学習
    predictor.train('ch06/train.txt')
    print("学習が完了しました。")
    
    return predictor

if __name__ == '__main__':
    model_train()
