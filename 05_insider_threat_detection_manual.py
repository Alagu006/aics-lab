"""
05_insider_threat_detection_manual.py - User Behavior Analytics (UBA) (CY3764 Manual)
REQUIRED PACKAGES:
  * pip install scikit-learn numpy
  * Tested on: pip 26.1.2 | scikit-learn==1.9.1 | numpy==2.2.4
"""
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.metrics import classification_report

np.random.seed(42)
normal = np.random.normal([15, 2, 5, 0.5], [3, 1, 1, 0.2], (1000, 4))
threat = np.random.normal([120, 25, 60, 8.0], [20, 5, 10, 1.5], (50, 4))
X = np.vstack([normal, threat])
y_true = np.array([1]*1000 + [-1]*50)

print(f"Generating synthetic user behavior data... Shape: {X.shape} | Threat users: 50")
iso = IsolationForest(contamination=0.05, random_state=42).fit(X)
y_pred = iso.predict(X)

print("=" * 55 + "\nINSIDER THREAT DETECTION RESULTS\n" + "=" * 55)
print(classification_report(y_true, y_pred, target_names=["Threat (-1)", "Normal (1)"], digits=4))
print(f"Threat Outliers Flagged: {sum(y_pred == -1)} out of {len(X)} records")

"""
SAMPLE OUTPUT:
Generating synthetic user behavior data... Shape: (1050, 4) | Threat users: 50
=======================================================
INSIDER THREAT DETECTION RESULTS
=======================================================
              precision    recall  f1-score   support
 Threat (-1)     0.8868    0.9400    0.9126        50
  Normal (1)     0.9970    0.9940    0.9955      1000
Threat Outliers Flagged: 53 out of 1050 records
"""
