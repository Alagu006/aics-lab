"""
05. Insider Threat Detection
Purpose: Identify unusual employee activity (files accessed, failed logins, after-hours activity).

REQUIRED PACKAGES:
  * pip install scikit-learn numpy
  * Tested on: pip 26.1.2 | scikit-learn==1.9.1 | numpy==2.2.4
"""
import numpy as np
from sklearn.ensemble import IsolationForest

rng = np.random.default_rng(2)
# Columns: [files accessed, failed logins, after-hours activity]
users = rng.normal([10, 2, 1], [3, 1, 0.5], (100, 3))

model = IsolationForest(contamination=0.05, random_state=2)
model.fit(users)

activity = [[12, 1, 0], [100, 20, 10], [9, 2, 1]]
for row, result in zip(activity, model.predict(activity)):
    print(f"Activity {row} -> {'[!] Suspicious (Outlier)' if result == -1 else '[+] Normal'}")

"""
SAMPLE OUTPUT:
Activity [12, 1, 0] -> [+] Normal
Activity [100, 20, 10] -> [!] Suspicious (Outlier)
Activity [9, 2, 1] -> [+] Normal
"""
