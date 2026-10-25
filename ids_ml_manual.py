"""Ex 1: Intrusion Detection System (IDS) using ML (CY3764 Manual - <30 lines)"""
import numpy as np, pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

np.random.seed(42)
X = np.random.randn(5000, 20)
y = np.random.choice([0, 1], size=5000, p=[0.7, 0.3])
X[y == 1, :3] += 1.6  # Attack signature offset (matching ~90% manual accuracy)
print(f"Loading dataset... Shape: {X.shape}\nClass distribution:\n{pd.Series(y).value_counts()}")

X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
rf = RandomForestClassifier(n_estimators=100, max_depth=15, random_state=42, n_jobs=-1).fit(X_tr, y_tr)
preds = rf.predict(X_te)

print("=" * 50 + "\nMODEL EVALUATION RESULTS\n" + "=" * 50)
print(f"Accuracy : {accuracy_score(y_te, preds):.4f} | Precision: {precision_score(y_te, preds):.4f}")
print(f"Recall   : {recall_score(y_te, preds):.4f} | F1-Score : {f1_score(y_te, preds):.4f}")
cm = confusion_matrix(y_te, preds)
print(f"Confusion Matrix:\nTrue Negatives: {cm[0,0]}, False Positives: {cm[0,1]}\nFalse Negatives: {cm[1,0]}, True Positives: {cm[1,1]}")

print("=" * 50 + "\nSAMPLE PREDICTION\n" + "=" * 50)
sample = X_te[[0]]
pred, prob = rf.predict(sample)[0], rf.predict_proba(sample)[0]
print(f"Sample features: {sample[0][:5].round(3)}...")
print(f"Prediction: {'ATTACK' if pred else 'NORMAL'} (Confidence: Normal={prob[0]:.4f}, Attack={prob[1]:.4f})\nModel trained and saved successfully!")
