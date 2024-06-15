from quiz52 import model_train
import pandas as pd
import numpy as np

def get_top_bottom_features(predictor, n=10):
    feature_names = predictor.vectorizer.get_feature_names_out()
    coefs = predictor.model.coef_

    # Get top n and bottom n features for each category
    top_features = []
    bottom_features = []
    for idx, category in predictor.inverse_label_mapping.items():
        coef = coefs[idx]
        top_n_idx = np.argsort(coef)[-n:]
        bottom_n_idx = np.argsort(coef)[:n]
        top_features.append((category, feature_names[top_n_idx], coef[top_n_idx]))
        bottom_features.append((category, feature_names[bottom_n_idx], coef[bottom_n_idx]))
    
    return top_features, bottom_features

def print_features(features, title):
    print(title)
    for category, feature_names, coefs in features:
        print(f"Category: {category}")
        for feature, coef in zip(feature_names, coefs):
            print(f"{feature}: {coef:.4f}")
        print()

def evaluate_model():
    # 52番のモデルをロードしてトレーニング
    predictor = model_train()
    
    # 重みの高い特徴量トップ10と低い特徴量トップ10を取得
    top_features, bottom_features = get_top_bottom_features(predictor)
    
    # 結果の表示
    print_features(top_features, "重みの高い特徴量トップ10:")
    print_features(bottom_features, "重みの低い特徴量トップ10:")
    
    return predictor

if __name__ == '__main__':
    evaluate_model()
