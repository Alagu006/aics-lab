# AI in Cyber Security Mini-Projects (Exam & Lab Revision Sheet)

This folder contains shortened, paper-friendly implementations of all 10 AI and cybersecurity mini-projects designed for rapid comprehension (~20–30 minutes per project).

## Master Package Installation & Requirements

| Mini-Project | Required `pip install` Command | Tested Versions |
| :--- | :--- | :--- |
| **01. Network IDS** | `pip install scapy` | `pip 26.1.2` \| `scapy>=2.5.0` |
| **02. Malware Classification** | `pip install scikit-learn numpy` | `pip 26.1.2` \| `scikit-learn==1.9.1` \| `numpy==2.2.4` |
| **03. Phishing Email Detection** | `pip install scikit-learn` | `pip 26.1.2` \| `scikit-learn==1.9.1` |
| **04. Network Anomaly Detection** | `pip install scikit-learn numpy` | `pip 26.1.2` \| `scikit-learn==1.9.1` \| `numpy==2.2.4` |
| **05. Insider Threat Detection** | `pip install scikit-learn numpy` | `pip 26.1.2` \| `scikit-learn==1.9.1` \| `numpy==2.2.4` |
| **06. Spam Detection** | `pip install scikit-learn` | `pip 26.1.2` \| `scikit-learn==1.9.1` |
| **07. Cyberattack Prediction** | `pip install pandas scikit-learn numpy` | `pip 26.1.2` \| `pandas==3.0.0` \| `scikit-learn==1.9.1` \| `numpy==2.2.4` |
| **08. Deep Learning Traffic Classifier**| `pip install tensorflow scikit-learn numpy` | `pip 26.1.2` \| `scikit-learn==1.9.1` \| `numpy==2.2.4` \| `tensorflow>=2.12.0` |
| **09. Secure AI Chat** | `pip install streamlit scikit-learn numpy` | `pip 26.1.2` \| `scikit-learn==1.9.1` \| `numpy==2.2.4` \| `streamlit>=1.28.0` |
| **10. Ransomware Detection** | `pip install scikit-learn numpy` | `pip 26.1.2` \| `scikit-learn==1.9.1` \| `numpy==2.2.4` |

---

## Directory Index

| File | Mini-Project | Main Algorithm / Library | Approx Time | Core Purpose |
| :--- | :--- | :--- | :--- | :--- |
| [`01_network_ids.py`](01_network_ids.py) | Network Intrusion Detection System | Scapy / TCP SYN Sniffer | 25 min | Detect possible TCP SYN port scans |
| [`02_malware_classification.py`](02_malware_classification.py) | Malware Classification | Random Forest (`sklearn`) | 20 min | Classify file feature vectors as benign or malware |
| [`03_phishing_email_detection.py`](03_phishing_email_detection.py) | Phishing Email Detection | TF-IDF + Naive Bayes | 20 min | Classify email texts as phishing or legitimate |
| [`04_network_anomaly_detection.py`](04_network_anomaly_detection.py) | Network Anomaly Detection | Isolation Forest | 20 min | Detect network traffic flow outliers |
| [`05_insider_threat_detection.py`](05_insider_threat_detection.py) | Insider Threat Detection | Isolation Forest | 20 min | Flag abnormal employee file access / after-hours activity |
| [`06_spam_detection.py`](06_spam_detection.py) | Spam Detection | CountVectorizer + Naive Bayes | 15 min | Classify SMS/chat messages as spam |
| [`07_cyberattack_prediction.py`](07_cyberattack_prediction.py) | Cyberattack Prediction | Time-Series Lags + Random Forest | 25 min | Predict attack presence in the next time window |
| [`08_deep_learning_traffic_classification.py`](08_deep_learning_traffic_classification.py) | Deep Learning Traffic Classification | Sequential Neural Net (TensorFlow / MLP) | 25 min | Classify traffic into Normal, DoS, and PortScan |
| [`09_secure_ai_chat.py`](09_secure_ai_chat.py) | Secure Chat with AI Anomaly Detection | Streamlit + SQLite + Isolation Forest | 30 min | Chat UI with SHA-256 auth and burst rate alerting |
| [`10_ransomware_detection.py`](10_ransomware_detection.py) | Ransomware Behaviour Detection | Isolation Forest | 20 min | Flag rapid file modifications & high entropy changes |

---

## Quick One-Liner Install for All Projects:
```bash
pip install scikit-learn numpy pandas scapy tensorflow streamlit
```
