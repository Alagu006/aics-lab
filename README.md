# Artificial Intelligence in Cyber Security Laboratory (CY3764)

This repository contains **20 Python files** (2 implementations for each of the 10 experiments):
- **Implementation A (`01_network_ids.py` ... `10_ransomware_detection.py`):** Shortened, paper-friendly implementations (~20–30 lines).
- **Implementation B (`01_ids_ml_manual.py` ... `10_ransomware_detection_manual.py`):** Compact implementations (<30 lines) matching the exact evaluation metrics and outputs from the official **CY3764 Laboratory Manual**.

---

## 20 Files Master Index

| Ex # | Experiment Title | File 1 (Mini-Project) | File 2 (Lab Manual Match) | Key Model / Algorithm |
| :---: | :--- | :--- | :--- | :--- |
| **01** | Intrusion Detection System (IDS) | [`01_network_ids.py`](01_network_ids.py) | [`01_ids_ml_manual.py`](01_ids_ml_manual.py) | Scapy SYN Sniffer / Random Forest (CICIDS2017) |
| **02** | Malware Family Classification | [`02_malware_classification.py`](02_malware_classification.py) | [`02_malware_classification_manual.py`](02_malware_classification_manual.py) | Feature Classifier / 5-Family Binary Image Classifier |
| **03** | Phishing Email Detection | [`03_phishing_email_detection.py`](03_phishing_email_detection.py) | [`03_phishing_email_detection_manual.py`](03_phishing_email_detection_manual.py) | TF-IDF + Naive Bayes / NLP Pipeline with Probabilities |
| **04** | Network Anomaly Detection | [`04_network_anomaly_detection.py`](04_network_anomaly_detection.py) | [`04_network_anomaly_detection_manual.py`](04_network_anomaly_detection_manual.py) | Isolation Forest / 95th Percentile Reconstruction Threshold |
| **05** | Insider Threat Detection (UBA) | [`05_insider_threat_detection.py`](05_insider_threat_detection.py) | [`05_insider_threat_detection_manual.py`](05_insider_threat_detection_manual.py) | Isolation Forest / User Behavioral Analytics Matrix |
| **06** | Spam Detection | [`06_spam_detection.py`](06_spam_detection.py) | [`06_spam_detection_manual.py`](06_spam_detection_manual.py) | CountVectorizer / Dual Model Comparison (NB vs SVM) |
| **07** | Cyberattack Prediction | [`07_cyberattack_prediction.py`](07_cyberattack_prediction.py) | [`07_cyberattack_prediction_manual.py`](07_cyberattack_prediction_manual.py) | Lagged RF Classifier / 3-Year Time-Series Forecasting |
| **08** | Network Traffic Classification | [`08_deep_learning_traffic_classification.py`](08_deep_learning_traffic_classification.py) | [`08_deep_learning_traffic_classification_manual.py`](08_deep_learning_traffic_classification_manual.py) | 3-Class Net / 7-Class Protocol Classifier (HTTP, DNS, etc.) |
| **09** | Secure Chat with AI Anomaly | [`09_secure_ai_chat.py`](09_secure_ai_chat.py) | [`09_secure_ai_chat_manual.py`](09_secure_ai_chat_manual.py) | Streamlit Web App / CLI Authentication & Velocity Anomaly Engine |
| **10** | Ransomware Behavior Detection | [`10_ransomware_detection.py`](10_ransomware_detection.py) | [`10_ransomware_detection_manual.py`](10_ransomware_detection_manual.py) | Behavioral Isolation Forest / Multi-Metric Telemetry Classifier |

---

## Required Dependencies

Install all dependencies in one command:
```bash
pip install scikit-learn numpy pandas scapy streamlit
```

---

## Documentation & Troubleshooting

- Refer to [**`EXPERIMENT_GUIDE_AND_TROUBLESHOOTING.md`**](EXPERIMENT_GUIDE_AND_TROUBLESHOOTING.md) for expected observations, potential errors, and step-by-step rectifications.
- Refer to [**`KALI_LINUX_RUN_GUIDE_AND_OUTPUTS.md`**](KALI_LINUX_RUN_GUIDE_AND_OUTPUTS.md) for terminal commands and outputs in Kali Linux.
