from quiz52 import model_train
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

class NewsCategoryPredictor:
    def __init__(self, C=1.0):
        self.model = LogisticRegression(C=C, max_iter=1000)
        self.vectorizer = CountVectorizer(max_features=1000)
        self.label_mapping = None
        self.inverse_label_mapping = None

    def load_data(self, label_file):
        labels_df = pd.read_csv(label_file, sep='\t', header=None, names=['CATEGORY', 'TITLE'])
        labels = labels_df['CATEGORY'].map(self.label_mapping)
        features = self.vectorizer.transform(labels_df['TITLE'])
        return features, labels

    def train(self, train_label_file):
        # ラベルを数値に変換
        train_labels_df = pd.read_csv(train_label_file, sep='\t', header=None, names=['CATEGORY', 'TITLE'])
        self.label_mapping = {label: idx for idx, label in enumerate(train_labels_df['CATEGORY'].unique())}
        self.inverse_label_mapping = {idx: label for label, idx in self.label_mapping.items()}
        
        # Vectorizerを学習
        self.vectorizer.fit(train_labels_df['TITLE'])
        
        train_features, train_labels = self.load_data(train_label_file)
        
        # モデルの学習
        self.model.fit(train_features, train_labels)
        
        return train_features, train_labels

def evaluate_model_with_different_C(train_file, val_file, test_file, C_values):
    train_accuracies = []
    val_accuracies = []
    test_accuracies = []
    
    for C in C_values:
        predictor = NewsCategoryPredictor(C=C)
        
        # 学習データを読み込み、モデルを学習
        train_features, train_labels = predictor.train(train_file)
        
        # 検証データと評価データの特徴量とラベルを読み込む
        val_features, val_labels = predictor.load_data(val_file)
        test_features, test_labels = predictor.load_data(test_file)
        
        # 学習データ、検証データ、評価データの正解率を計算
        train_accuracy = accuracy_score(train_labels, predictor.model.predict(train_features))
        val_accuracy = accuracy_score(val_labels, predictor.model.predict(val_features))
        test_accuracy = accuracy_score(test_labels, predictor.model.predict(test_features))
        
        train_accuracies.append(train_accuracy)
        val_accuracies.append(val_accuracy)
        test_accuracies.append(test_accuracy)
    
    return train_accuracies, val_accuracies, test_accuracies

def plot_accuracies(C_values, train_accuracies, val_accuracies, test_accuracies):
    plt.figure(figsize=(10, 6))
    plt.plot(C_values, train_accuracies, label='Train Accuracy')
    plt.plot(C_values, val_accuracies, label='Validation Accuracy')
    plt.plot(C_values, test_accuracies, label='Test Accuracy')
    plt.xscale('log')
    plt.xlabel('Regularization Parameter (C)')
    plt.ylabel('Accuracy')
    plt.title('Effect of Regularization Parameter on Accuracy')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    train_file = 'ch06/train.txt'
    val_file = 'ch06/valid.txt'  # Assuming there is a separate validation file
    test_file = 'ch06/test.txt'
    
    C_values = [0.01, 0.1, 1, 10, 100]
    
    train_accuracies, val_accuracies, test_accuracies = evaluate_model_with_different_C(train_file, val_file, test_file, C_values)
    
    plot_accuracies(C_values, train_accuracies, val_accuracies, test_accuracies)
