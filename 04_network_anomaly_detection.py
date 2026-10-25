"""
04. Network Anomaly Detection
Purpose: Flag unusual network-flow measurements using Isolation Forest.

REQUIRED PACKAGES:
  * pip install scikit-learn numpy
  * Tested on: pip 26.1.2 | scikit-learn==1.9.1 | numpy==2.2.4
"""
import numpy as np
from sklearn.ensemble import IsolationForest

rng = np.random.default_rng(1)
normal = rng.normal(50, 10, (200, 2))  # Baseline flow features (e.g., packet rate, flow size)

model = IsolationForest(contamination=0.05, random_state=1)
model.fit(normal)

flows = [[52, 48], [300, 400], [45, 55]]
for flow, result in zip(flows, model.predict(flows)):
    print(f"Flow {flow} -> {'[!] Anomaly' if result == -1 else '[+] Normal'}")

"""
SAMPLE OUTPUT:
Flow [52, 48] -> [+] Normal
Flow [300, 400] -> [!] Anomaly
Flow [45, 55] -> [+] Normal
"""
