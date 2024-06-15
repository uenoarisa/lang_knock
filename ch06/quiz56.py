from quiz52 import model_train
import pandas as pd
from sklearn.metrics import accuracy_score, precision_recall_fscore_support

class NewsCategoryEvaluator:
    def __init__(self, predictor):
        self.predictor = predictor

    def evaluate(self, label_file):
        features, labels = self.predictor.load_data(label_file)
        predictions = self.predictor.model.predict(features)
        accuracy = accuracy_score(labels, predictions)
        return accuracy, labels, predictions

    def calculate_metrics(self, labels, predictions):
        precision, recall, f1, _ = precision_recall_fscore_support(labels, predictions, average=None)
        precision_micro, recall_micro, f1_micro, _ = precision_recall_fscore_support(labels, predictions, average='micro')
        precision_macro, recall_macro, f1_macro, _ = precision_recall_fscore_support(labels, predictions, average='macro')
        
        return {
            'precision': precision,
            'recall': recall,
            'f1': f1,
            'precision_micro': precision_micro,
            'recall_micro': recall_micro,
            'f1_micro': f1_micro,
            'precision_macro': precision_macro,
            'recall_macro': recall_macro,
            'f1_macro': f1_macro,
        }

def evaluate_model():
    # 52番のモデルをロードしてトレーニング
    predictor = model_train()
    
    # Evaluatorのインスタンス化
    evaluator = NewsCategoryEvaluator(predictor)
    
    # 評価データでの正解率と予測結果の計測
    test_accuracy, test_labels, test_predictions = evaluator.evaluate('ch06/test.txt')
    print(f"評価データの正解率: {test_accuracy:.2f}")
    
    # 適合率，再現率，F1スコアの計測
    metrics = evaluator.calculate_metrics(test_labels, test_predictions)
    print("カテゴリごとの適合率，再現率，F1スコア:")
    for idx, category in predictor.inverse_label_mapping.items():
        print(f"{category} - 適合率: {metrics['precision'][idx]:.2f}, 再現率: {metrics['recall'][idx]:.2f}, F1スコア: {metrics['f1'][idx]:.2f}")
    
    print(f"マイクロ平均 - 適合率: {metrics['precision_micro']:.2f}, 再現率: {metrics['recall_micro']:.2f}, F1スコア: {metrics['f1_micro']:.2f}")
    print(f"マクロ平均 - 適合率: {metrics['precision_macro']:.2f}, 再現率: {metrics['recall_macro']:.2f}, F1スコア: {metrics['f1_macro']:.2f}")
    
    return predictor

if __name__ == '__main__':
    evaluate_model()
