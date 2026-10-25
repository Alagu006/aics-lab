"""
10. Ransomware Detection Using Behaviour Analysis
Purpose: Detect suspicious file activity (rapid modification/entropy) using Isolation Forest.

REQUIRED PACKAGES:
  * pip install scikit-learn numpy
  * Tested on: pip 26.1.2 | scikit-learn==1.9.1 | numpy==2.2.4
"""
import numpy as np
from sklearn.ensemble import IsolationForest

# Features: [files modified/min, rename count, entropy change]
rng = np.random.default_rng(10)
normal = np.clip(rng.normal([5, 2, 0.1], [2, 1, 0.05], (200, 3)), 0, None)

model = IsolationForest(contamination=0.05, random_state=1)
model.fit(normal)

# Sample file activities (e.g., normal activity vs mass-encryption)
activity = np.array([
    [4, 2, 0.1],      # Normal work
    [150, 100, 0.9],  # Rapid mass modification/encryption
    [8, 3, 0.2]       # Normal task
])

for feat, result in zip(activity, model.predict(activity)):
    print(f"Activity {feat.tolist()} -> {'[!] Possible Ransomware' if result == -1 else '[+] Normal Activity'}")

"""
SAMPLE OUTPUT:
Activity [4.0, 2.0, 0.1] -> [+] Normal Activity
Activity [150.0, 100.0, 0.9] -> [!] Possible Ransomware
Activity [8.0, 3.0, 0.2] -> [!] Possible Ransomware
"""
