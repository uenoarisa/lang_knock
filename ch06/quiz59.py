import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split, GridSearchCV

class NewsCategoryPredictor:
    def __init__(self, model):
        self.model = model
        self.vectorizer = CountVectorizer(max_features=1000)
        self.label_mapping = None
        self.inverse_label_mapping = None

    def load_data(self, label_file):
        labels_df = pd.read_csv(label_file, sep='\t', header=None, names=['CATEGORY', 'TITLE'])
        labels = labels_df['CATEGORY'].map(self.label_mapping)
        features = self.vectorizer.transform(labels_df['TITLE'])
        return features, labels

    def train(self, train_label_file):
        train_labels_df = pd.read_csv(train_label_file, sep='\t', header=None, names=['CATEGORY', 'TITLE'])
        self.label_mapping = {label: idx for idx, label in enumerate(train_labels_df['CATEGORY'].unique())}
        self.inverse_label_mapping = {idx: label for label, idx in self.label_mapping.items()}
        
        self.vectorizer.fit(train_labels_df['TITLE'])
        train_features, train_labels = self.load_data(train_label_file)
        self.model.fit(train_features, train_labels)
        return train_features, train_labels

def evaluate_model_with_hyperparameter_search(train_file, val_file, test_file):
    train_labels_df = pd.read_csv(train_file, sep='\t', header=None, names=['CATEGORY', 'TITLE'])
    val_labels_df = pd.read_csv(val_file, sep='\t', header=None, names=['CATEGORY', 'TITLE'])
    test_labels_df = pd.read_csv(test_file, sep='\t', header=None, names=['CATEGORY', 'TITLE'])
    
    vectorizer = CountVectorizer(max_features=1000)
    vectorizer.fit(train_labels_df['TITLE'])
    
    X_train = vectorizer.transform(train_labels_df['TITLE'])
    y_train = train_labels_df['CATEGORY'].factorize()[0]
    
    X_val = vectorizer.transform(val_labels_df['TITLE'])
    y_val = val_labels_df['CATEGORY'].factorize()[0]
    
    X_test = vectorizer.transform(test_labels_df['TITLE'])
    y_test = test_labels_df['CATEGORY'].factorize()[0]
    
    models = [
        ('LogisticRegression', LogisticRegression(max_iter=1000), {'C': [0.01, 0.1, 1, 10, 100]}),
        ('RandomForest', RandomForestClassifier(), {'n_estimators': [10, 50, 100, 200]}),
        ('SVM', SVC(), {'C': [0.01, 0.1, 1, 10, 100]})
    ]
    
    best_model = None
    best_score = 0
    best_params = None
    
    for name, model, params in models:
        grid = GridSearchCV(model, params, cv=5)
        grid.fit(X_train, y_train)
        
        val_score = grid.score(X_val, y_val)
        if val_score > best_score:
            best_score = val_score
            best_model = grid.best_estimator_
            best_params = grid.best_params_
    
    # 最良モデルでテストデータの正解率を計算
    test_accuracy = best_model.score(X_test, y_test)
    
    print(f"Best Model: {best_model}")
    print(f"Best Parameters: {best_params}")
    print(f"Validation Accuracy: {best_score:.2f}")
    print(f"Test Accuracy: {test_accuracy:.2f}")

if __name__ == '__main__':
    train_file = 'ch06/train.txt'
    val_file = 'ch06/valid.txt'
    test_file = 'ch06/test.txt'
    
    evaluate_model_with_hyperparameter_search(train_file, val_file, test_file)
