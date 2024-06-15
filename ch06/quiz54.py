from quiz52 import model_train
import pandas as pd
from sklearn.metrics import accuracy_score

class NewsCategoryEvaluator:
    def __init__(self, predictor):
        self.predictor = predictor

    def evaluate(self, label_file):
        features, labels = self.predictor.load_data(label_file)
        predictions = self.predictor.model.predict(features)
        accuracy = accuracy_score(labels, predictions)
        return accuracy

def evaluate_model():
    # 52番のモデルをロードしてトレーニング
    predictor = model_train()
    
    # Evaluatorのインスタンス化
    evaluator = NewsCategoryEvaluator(predictor)
    
    # 学習データでの正解率の計測
    train_accuracy = evaluator.evaluate('ch06/train.txt')
    print(f"学習データの正解率: {train_accuracy:.2f}")
    
    # 評価データでの正解率の計測
    test_accuracy = evaluator.evaluate('ch06/test.txt')
    print(f"評価データの正解率: {test_accuracy:.2f}")
    
    return predictor

if __name__ == '__main__':
    evaluate_model()
