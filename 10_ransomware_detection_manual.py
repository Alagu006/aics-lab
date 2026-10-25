"""
10_ransomware_detection_manual.py - Ransomware Behavioral Detector (CY3764 Manual)
REQUIRED PACKAGES:
  * pip install scikit-learn numpy
  * Tested on: pip 26.1.2 | scikit-learn==1.9.1 | numpy==2.2.4
"""
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

np.random.seed(42)
normal = np.random.normal([5, 2, 0.1, 1], [2, 1, 0.05, 0.5], (700, 4))
ransom = np.random.normal([180, 120, 0.85, 8], [30, 20, 0.1, 2.0], (300, 4))
X = np.clip(np.vstack([normal, ransom]), 0, None)
y = np.array([0] * 700 + [1] * 300)

print(f"Generating synthetic behavioral data... Samples: {len(X)} | Normal: 700 | Ransomware: 300")
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
rf = RandomForestClassifier(n_estimators=50, random_state=42).fit(X_tr, y_tr)
preds = rf.predict(X_te)

print("=" * 55 + "\nRANSOMWARE DETECTION RESULTS\n" + "=" * 55)
print(f"Detection Accuracy: {accuracy_score(y_te, preds)*100:.2f}%\n")
print(classification_report(y_te, preds, target_names=["Normal", "Ransomware"], digits=4))

test_proc = [[160, 110, 0.9, 7]]
print(f"Test Telemetry {test_proc[0]} -> Prediction: {'[!] RANSOMWARE DETECTED' if rf.predict(test_proc)[0] else '[+] NORMAL'}")

"""
SAMPLE OUTPUT:
Generating synthetic behavioral data... Samples: 1000 | Normal: 700 | Ransomware: 300
=======================================================
RANSOMWARE DETECTION RESULTS
=======================================================
Detection Accuracy: 100.00%

              precision    recall  f1-score   support
      Normal     1.0000    1.0000    1.0000       140
  Ransomware     1.0000    1.0000    1.0000        60

Test Telemetry [160, 110, 0.9, 7] -> Prediction: [!] RANSOMWARE DETECTED
"""
