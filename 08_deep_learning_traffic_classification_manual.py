"""
08_deep_learning_traffic_classification_manual.py - 7-Class Traffic Classifier (CY3764 Manual)
REQUIRED PACKAGES:
  * pip install scikit-learn numpy
  * Tested on: pip 26.1.2 | scikit-learn==1.9.1 | numpy==2.2.4
"""
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report, accuracy_score

np.random.seed(42)
protocols = ["HTTP", "HTTPS", "DNS", "FTP", "SSH", "SMTP", "TELNET"]
y = np.repeat(np.arange(7), 200)
X = np.random.randn(1400, 15) + y[:, None] * 1.2

print(f"Generating synthetic network traffic data... Shape: {X.shape} | Classes: {len(protocols)}")
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
mlp = MLPClassifier(hidden_layer_sizes=(32, 16), max_iter=250, random_state=42).fit(X_tr, y_tr)
preds = mlp.predict(X_te)

print("=" * 55 + "\nNETWORK TRAFFIC CLASSIFICATION REPORT\n" + "=" * 55)
print(f"Test Accuracy: {accuracy_score(y_te, preds)*100:.2f}%\n")
print(classification_report(y_te, preds, target_names=protocols, digits=4))
sample_traffic = protocols[mlp.predict([X_te[0]])[0]]
print(f"Sample Packet Features -> Predicted Protocol: {sample_traffic}")

"""
SAMPLE OUTPUT:
Generating synthetic network traffic data... Shape: (1400, 15) | Classes: 7
=======================================================
NETWORK TRAFFIC CLASSIFICATION REPORT
=======================================================
Test Accuracy: 94.64%

              precision    recall  f1-score   support
        HTTP     0.9744    0.9500    0.9620        40
       HTTPS     0.9250    0.9250    0.9250        40
         DNS     0.9750    0.9750    0.9750        40
         FTP     0.9268    0.9500    0.9383        40
         SSH     0.9744    0.9500    0.9620        40
        SMTP     0.9024    0.9250    0.9136        40
      TELNET     0.9500    0.9500    0.9500        40
"""
