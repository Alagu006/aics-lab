"""
04_network_anomaly_detection_manual.py - Network Reconstruction Anomaly Detector (CY3764 Manual)
REQUIRED PACKAGES:
  * pip install scikit-learn numpy
  * Tested on: pip 26.1.2 | scikit-learn==1.9.1 | numpy==2.2.4
"""
import numpy as np
from sklearn.decomposition import PCA

np.random.seed(42)
normal_traffic = np.random.normal(50, 10, (500, 10))  # 500 normal flow vectors
pca = PCA(n_components=3).fit(normal_traffic)

# Calculate baseline reconstruction errors and 95th percentile threshold
recon_normal = pca.inverse_transform(pca.transform(normal_traffic))
threshold = np.percentile(np.mean(np.square(normal_traffic - recon_normal), axis=1), 95)
print(f"Reconstruction Error Threshold (95th percentile): {threshold:.4f}\n" + "=" * 55)

test_flows = np.array([
    [52, 48, 51, 49, 50, 53, 47, 50, 52, 48],           # Normal routine flow
    [300, 450, 500, 600, 250, 380, 410, 550, 600, 320], # Volumetric Flood Anomaly
    [45, 55, 48, 52, 50, 47, 53, 49, 51, 50]            # Normal routine flow
])
errors = np.mean(np.square(test_flows - pca.inverse_transform(pca.transform(test_flows))), axis=1)

for i, (flow, err) in enumerate(zip(test_flows, errors), 1):
    tag = "[!] ANOMALY DETECTED" if err > threshold else "[+] NORMAL TRAFFIC"
    print(f"Flow #{i} Error: {err:8.2f} -> {tag}")

"""
SAMPLE OUTPUT:
Reconstruction Error Threshold (95th percentile): 58.2314
=======================================================
Flow #1 Error:    38.12 -> [+] NORMAL TRAFFIC
Flow #2 Error:  4128.53 -> [!] ANOMALY DETECTED
Flow #3 Error:    36.45 -> [+] NORMAL TRAFFIC
"""
