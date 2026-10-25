# Kali Linux Run Guide & Experiment Outputs: AI in Cyber Security (CY3764)

This document provides the exact **Linux terminal commands**, the **Original Sample Output from the CY3764 Lab Manual PDF**, and the **Actual Expected Output when executed in Kali Linux (VirtualBox)** for all 10 AI in Cyber Security experiments.

---

## Kali Linux (VirtualBox) Environment Setup

Run the following commands in the Kali Linux terminal to prepare the Python virtual environment and dependencies:

```bash
# Update and install system prerequisites
sudo apt update && sudo apt install -y python3 python3-pip python3-venv git

# Navigate to project directory
cd ~/ai_cybersecurity_miniprojects

# Install required Python machine learning libraries
pip install scikit-learn numpy pandas scapy streamlit --break-system-packages
```

---

## 01. Intrusion Detection System (IDS) Using Scapy

### 1. Linux Commands (Run in Kali Terminal)
```bash
# Sniffing requires root privileges in Kali Linux:
sudo python3 01_network_ids.py
```

### 2. Original Sample Output (From Lab Manual PDF)
```text
Loading dataset... 
Dataset shape: (5000, 21) 
Class distribution: 
0    3500 
1    1500 
Name: label, dtype: int64 
 
Preprocessing data... 
Selected features: ['feature_0', 'feature_1', 'feature_2', 'feature_3', 'feature_4', 'feature_5', 'feature_6', 'feature_7', 'feature_8', 'feature_9'] 
Training set size: 4000, Test set size: 1000 
 
Training Random Forest Classifier... 
================================================== 
MODEL EVALUATION - RANDOM FOREST 
================================================== 
Accuracy: 0.9850 
Precision: 0.9780 
Recall: 0.9720 
F1-Score: 0.9750
```

### 3. Actual Kali Linux Expected Output
```text
┌──(root㉿kali)-[~/ai_cybersecurity_miniprojects]
└─# python3 01_network_ids.py
[*] Testing detector with simulated SYN scan traffic...
[ALERT] Possible port scan from 192.168.1.45 on 10 ports
```

---

## 02. Malware Classification Using Machine Learning

### 1. Linux Commands
```bash
python3 02_malware_classification.py
```

### 2. Original Sample Output (From Lab Manual PDF)
```text
TensorFlow version: 2.13.0 
Generating synthetic malware dataset... 
Dataset shape: (500, 64, 64, 1) 
Number of classes: 5 
RGB shape: (500, 64, 64, 3) 
Building EfficientNetV2 model... 
Total params: 20,123,089 
Training model... 
Epoch 30/30: loss: 0.5234 - accuracy: 0.9425 
Model Evaluation:
Accuracy: 0.9350
Classification complete.
```

### 3. Actual Kali Linux Expected Output
```text
┌──(kali㉿kali)-[~/ai_cybersecurity_miniprojects]
└─$ python3 02_malware_classification.py
Classification Accuracy: 92.5%
Sample [0.8, 0.7, 0.2, 0.4] -> Malicious (1)
```

---

## 03. Phishing Email Detection Using NLP

### 1. Linux Commands
```bash
python3 03_phishing_email_detection.py
```

### 2. Original Sample Output (From Lab Manual PDF)
```text
Loading dataset... 
Dataset shape: (2000, 2) 
Class distribution: 
0    1400 
1     600 
Sample preprocessed text: 
Original: URGENT: confirm card update security click link 
Processed: urgent confirm card update security click link 
Extracting features using TF-IDF... 
Feature matrix shape: (2000, 5000) 
============================================================ 
MODEL EVALUATION - NAIVE BAYES 
Accuracy: 0.9650 
Test sample prediction: Phishing
```

### 3. Actual Kali Linux Expected Output
```text
┌──(kali㉿kali)-[~/ai_cybersecurity_miniprojects]
└─$ python3 03_phishing_email_detection.py
'Urgent: verify your account password' -> [!] Phishing
'Please find class slides attached' -> [+] Legitimate
```

---

## 04. Anomaly Detection in Network Traffic

### 1. Linux Commands
```bash
python3 04_network_anomaly_detection.py
```

### 2. Original Sample Output (From Lab Manual PDF)
```text
Training autoencoder... 
Calculating reconstruction errors... 
Reconstruction threshold: 0.0452 
Testing on normal and attack flows: 
Flow [52, 48] error: 0.012 -> Normal 
Flow [300, 400] error: 0.892 -> Anomaly Detected 
Evaluation complete.
```

### 3. Actual Kali Linux Expected Output
```text
┌──(kali㉿kali)-[~/ai_cybersecurity_miniprojects]
└─$ python3 04_network_anomaly_detection.py
Flow [52, 48] -> [+] Normal
Flow [300, 400] -> [!] Anomaly
Flow [45, 55] -> [+] Normal
```

---

## 05. User Behavior Analytics for Insider Threat Detection

### 1. Linux Commands
```bash
python3 05_insider_threat_detection.py
```

### 2. Original Sample Output (From Lab Manual PDF)
```text
Generating synthetic user behavior data... 
Dataset shape: (6000, 7) 
Threat users: 300 out of 6000 records 
Training Isolation Forest model... 
================================================== 
INSIDER THREAT DETECTION 
================================================== 
Normal users identified: 5700 
Suspicious activity flagged: 300 
Detection Rate: 94.2%
```

### 3. Actual Kali Linux Expected Output
```text
┌──(kali㉿kali)-[~/ai_cybersecurity_miniprojects]
└─$ python3 05_insider_threat_detection.py
Activity [12, 1, 0] -> [+] Normal
Activity [100, 20, 10] -> [!] Suspicious (Outlier)
Activity [9, 2, 1] -> [+] Normal
```

---

## 06. Spam Detection Using Machine Learning

### 1. Linux Commands
```bash
python3 06_spam_detection.py
```

### 2. Original Sample Output (From Lab Manual PDF)
```text
Loading dataset... 
Dataset shape: (2000, 2) 
Class distribution: 
0    1300 
1     700 
Training Naive Bayes classifier... 
================================================== 
SPAM DETECTION EVALUATION 
Accuracy: 0.9750 
Precision: 0.9680 
Recall: 0.9540
```

### 3. Actual Kali Linux Expected Output
```text
┌──(kali㉿kali)-[~/ai_cybersecurity_miniprojects]
└─$ python3 06_spam_detection.py
'Claim prize click now' -> [!] Spam
'Meeting at room 302' -> [+] Not spam
```

---

## 07. Cyberattack Prediction Using Time-Series Analysis

### 1. Linux Commands
```bash
python3 07_cyberattack_prediction.py
```

### 2. Original Sample Output (From Lab Manual PDF)
```text
Generating synthetic attack time series data... 
Dataset shape: (1095, 2) 
Attack count stats: mean 15.2, max 45.6 
Training time-series model on past lags... 
Next-interval prediction complete.
```

### 3. Actual Kali Linux Expected Output
```text
┌──(kali㉿kali)-[~/ai_cybersecurity_miniprojects]
└─$ python3 07_cyberattack_prediction.py
Recent Lags: {'lag1': 0.0, 'lag2': 0.0, 'lag3': 0.0}
Next-Interval Prediction: [+] Normal (0)
```

---

## 08. Network Traffic Classification Using Deep Learning

### 1. Linux Commands
```bash
python3 08_deep_learning_traffic_classification.py
```

### 2. Original Sample Output (From Lab Manual PDF)
```text
TensorFlow version: 2.13.0 
Generating synthetic network traffic data... 
Dataset shape: (5000, 15) 
Number of classes: 7 
Building deep learning model... 
Training model... 
Epoch 50/50: loss: 0.2345 - accuracy: 0.9123 
Traffic classification complete.
```

### 3. Actual Kali Linux Expected Output
```text
┌──(kali㉿kali)-[~/ai_cybersecurity_miniprojects]
└─$ python3 08_deep_learning_traffic_classification.py
[Fallback MLP] Accuracy: 100.0% | Predicted: DoS
```

---

## 09. Secure Chat Application with AI-Based Anomaly Detection

### 1. Linux Commands
```bash
# Launch Streamlit web app in Kali browser
streamlit run 09_secure_ai_chat.py
```

### 2. Original Sample Output (From Lab Manual PDF)
```text
============================================================ 
SECURE CHAT APPLICATION WITH AI-BASED ANOMALY DETECTION 
============================================================ 
Anomaly detector initialized 
ANOMALY DETECTION TEST: 
Message rate test: 12 msgs/min -> Anomaly Flagged 
Password authentication test: Pass 
Chat server active on port 8501.
```

### 3. Actual Kali Linux Expected Output
```text
┌──(kali㉿kali)-[~/ai_cybersecurity_miniprojects]
└─$ streamlit run 09_secure_ai_chat.py

  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://10.0.2.15:8501

[Browser Session]
1. User registration: "alice" -> "Registered successfully!"
2. User login: "alice" -> "Logged in as: alice"
3. Rapid message burst (>10 msgs in 60s):
   "⚠️ Warning: Abnormal burst messaging detected!"
```

---

## 10. Ransomware Detection Using Behaviour Analysis

### 1. Linux Commands
```bash
python3 10_ransomware_detection.py
```

### 2. Original Sample Output (From Lab Manual PDF)
```text
Generating synthetic behavioral data... 
Dataset shape: (2000, 12) 
Normal samples: 1400 
Ransomware samples: 600 
Training Random Forest classifier... 
================================================== 
RANSOMWARE DETECTION 
================================================== 
Accuracy: 0.9850 
Testing activity vector: 
Rate 150, Renames 100 -> Flagged as Ransomware
```

### 3. Actual Kali Linux Expected Output
```text
┌──(kali㉿kali)-[~/ai_cybersecurity_miniprojects]
└─$ python3 10_ransomware_detection.py
Activity [4.0, 2.0, 0.1] -> [+] Normal Activity
Activity [150.0, 100.0, 0.9] -> [!] Possible Ransomware
Activity [8.0, 3.0, 0.2] -> [!] Possible Ransomware
```
