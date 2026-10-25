# AI in Cyber Security: Mini-Project Guide & Troubleshooting Manual

This reference manual explains **what to look out for**, **potential errors**, and **exact rectifications** for each of the 10 AI in Cyber Security mini-projects in [`ai_cybersecurity_miniprojects/`](file:///d:/lab%20for%207th%20sem/ai_cybersecurity_miniprojects).

---

## Quick Reference Summary

| # | Project Name | Algorithm / Library | Key Observation | Common Error & Quick Fix |
| :-: | :--- | :--- | :--- | :--- |
| **01** | Network IDS | Scapy TCP Sniffer | `[ALERT] Possible port scan` | `No libpcap provider` $\rightarrow$ Install Npcap or run simulated mode |
| **02** | Malware Classification | Random Forest | Accuracy score (~90%+) | Input shape mismatch $\rightarrow$ Ensure 4 feature columns |
| **03** | Phishing Email Detection | TF-IDF + Naive Bayes | `[!] Phishing` vs `[+] Legitimate` | Vocabulary out-of-bounds $\rightarrow$ Retrain with diverse vocabulary |
| **04** | Network Anomaly Detection | Isolation Forest | Anomaly (-1) vs Normal (1) | Contamination parameter too high $\rightarrow$ Tune `contamination=0.01-0.05` |
| **05** | Insider Threat Detection | Isolation Forest | Flagged statistical outliers | Misinterpreting outlier as crime $\rightarrow$ Treat as anomaly alert |
| **06** | Spam Detection | CountVectorizer + NB | Message classification | Case sensitivity $\rightarrow$ Vectorizer lowercases by default |
| **07** | Cyberattack Prediction | Time-Series + RF | Next-interval attack (0/1) | `NaN` values after shifting $\rightarrow$ Use `df.dropna()` |
| **08** | DL Traffic Classifier | Sequential / MLP | 3-class prediction | TensorFlow missing $\rightarrow$ Automatic MLP fallback included |
| **09** | Secure AI Chat | Streamlit + SQLite | UI login & rate alert | SQLite threading lock $\rightarrow$ Use `check_same_thread=False` |
| **10** | Ransomware Detection | Isolation Forest | Rapid modification flag | False positives on bulk file copy $\rightarrow$ Combine rate with entropy |

---

## Project-by-Project Breakdown

### 01. Network Intrusion Detection System (IDS)
- **What to Look Out For:**
  - Detection of SYN scans: Packets where `SYN` flag (bit 2) is set and `ACK` flag (bit 16) is NOT set.
  - Threshold alert: Once an IP targets 10 unique destination ports within a 10-second window, the detector triggers an `[ALERT] Possible port scan`.
- **Potential Errors:**
  1. `WARNING: No libpcap provider available ! pcap won't be used` (Windows): Scapy cannot find WinPcap or Npcap for raw socket capture.
  2. `PermissionError: [WinError 10013] An attempt was made to access a socket in a way forbidden by its access permissions`: Raw packet sniffing requires Administrator (Windows) or root (`sudo`) privileges (Linux).
  3. Script hangs silently: On a quiet network with no incoming TCP packets, `sniff()` waits indefinitely.
- **How to Rectify:**
  - Install **Npcap** on Windows (enable "WinPcap API-compatible Mode" during installation).
  - On Linux/Kali, execute with elevated rights: `sudo python3 01_network_ids.py`.
  - Use the built-in synthetic packet test included in our script to verify detection logic immediately without waiting for network packets.

---

### 02. Malware Classification
- **What to Look Out For:**
  - Training/Test split accuracy (typically between 88% and 96%).
  - Test prediction on sample feature vector `[0.8, 0.7, 0.2, 0.4]` outputting `Malicious (1)`.
- **Potential Errors:**
  1. `ValueError: Expected 2D array, got 1D array instead`: Passing a single sample like `[0.8, 0.7, 0.2, 0.4]` instead of `[[0.8, 0.7, 0.2, 0.4]]`.
  2. `ModuleNotFoundError: No module named 'sklearn'`: `scikit-learn` is not installed.
- **How to Rectify:**
  - Install: `pip install scikit-learn numpy`.
  - Always wrap single prediction samples in a 2D list: `model.predict([[f1, f2, f3, f4]])`.

---

### 03. Phishing Email Detection
- **What to Look Out For:**
  - Correct classification of urgency/financial triggers ("verify bank account", "claim reward", "urgent") as `Phishing`.
  - Correct classification of routine communication ("meeting tomorrow", "notes attached") as `Legitimate`.
- **Potential Errors:**
  1. False negatives on unseen words: A tiny training set (6 emails) cannot generalize to vocabulary it has never encountered.
  2. Vectorizer shape mismatch when trying to transform manually.
- **How to Rectify:**
  - Use `make_pipeline(TfidfVectorizer(), MultinomialNB())` (as used in our script) so tokenization, vocabulary mapping, and inference are bundled into a single object.
  - Expand training list with more labeled sentences for classroom demonstrations.

---

### 04. Network Anomaly Detection
- **What to Look Out For:**
  - Baseline normal flows centered around `[50, 50]` labeled as `Normal (1)`.
  - Extreme values such as `[300, 400]` flagged as `[!] Anomaly (-1)`.
- **Potential Errors:**
  1. `ValueError: contamination must be in (0, 0.5]`: Setting an invalid contamination ratio.
  2. Normal data getting flagged as anomalies if standard deviation in training data is too small.
- **How to Rectify:**
  - Set `contamination=0.05` (assumes ~5% of traffic may be anomalous).
  - Train only on verified benign traffic baselines.

---

### 05. Insider Threat Detection
- **What to Look Out For:**
  - Multi-dimensional behavioral tracking: files accessed, failed logins, after-hours sessions.
  - Regular employees `[12, 1, 0]` marked normal; anomalous employee `[100, 20, 10]` flagged suspicious.
- **Potential Errors:**
  1. Over-flagging legitimate administrators performing routine maintenance or batch backups.
- **How to Rectify:**
  - In real deployments, baseline metrics must be grouped by employee role (e.g., developers vs. HR vs. sysadmins) rather than applying one uniform threshold.

---

### 06. Spam Detection
- **What to Look Out For:**
  - Fast Bag-of-Words text classification using `CountVectorizer`.
  - Keyword triggers like "cash", "prize", "free", "money" triggering spam predictions.
- **Potential Errors:**
  1. `IndexError` if input string is empty or contains only non-alphanumeric punctuation.
- **How to Rectify:**
  - Add simple input validation check: `if text.strip(): ...`.

---

### 07. Cyberattack Prediction (Time-Series Analysis)
- **What to Look Out For:**
  - Feature engineering using lagged time steps (`lag1`, `lag2`, `lag3`).
  - Prediction of state in step $t+1$ based on historical patterns.
- **Potential Errors:**
  1. `ValueError: Input contains NaN`: Occurs if `df.dropna()` is omitted after calling `df["attack"].shift(lag)`.
  2. Data leakage: Shuffling time-series data using `random_state` rather than sequential train/test split.
- **How to Rectify:**
  - Always call `df.dropna()` immediately after generating lag columns.
  - Use sequential splitting: `split = int(len(df) * 0.8)` to preserve temporal chronology.

---

### 08. Network Traffic Classification Using Deep Learning
- **What to Look Out For:**
  - 3-class multi-classification: Normal (0), DoS (1), PortScan (2).
  - Normalization using `StandardScaler` ensuring fast gradient convergence.
- **Potential Errors:**
  1. `ModuleNotFoundError: No module named 'tensorflow'`: TensorFlow is large (~500 MB) and may not be installed.
  2. `ValueError: Shapes (None, 1) and (None, 3) are incompatible`: Using `categorical_crossentropy` instead of `sparse_categorical_crossentropy` for integer labels.
- **How to Rectify:**
  - Our script includes an automatic fallback to `sklearn.neural_network.MLPClassifier`, allowing it to run smoothly on any machine with or without TensorFlow installed.

---

### 09. Secure Chat with AI-Based Anomaly Detection
- **What to Look Out For:**
  - Web UI at `http://localhost:8501`.
  - User registration with cryptographic SHA-256 password hashing.
  - Messaging velocity monitoring: if a user sends $>10$ messages in 60 seconds, an anomaly alert triggers.
- **Potential Errors:**
  1. `sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread`: Streamlit runs multi-threaded user sessions.
  2. `ModuleNotFoundError: No module named 'streamlit'`.
- **How to Rectify:**
  - Initialize SQLite with `sqlite3.connect("chat.db", check_same_thread=False)`.
  - Install: `pip install streamlit`.
  - Run with Streamlit CLI: `streamlit run ai_cybersecurity_miniprojects/09_secure_ai_chat.py`.

---

### 10. Ransomware Detection Using Behaviour Analysis
- **What to Look Out For:**
  - Combined metric tracking: file modification rate, rename frequency, and entropy changes.
  - Normal edits `[4.0, 2.0, 0.1]` marked normal; massive rapid encryption `[150.0, 100.0, 0.9]` flagged as `[!] Possible Ransomware`.
- **Potential Errors:**
  1. High entropy false positives: Compressing archives (ZIP/7z) or downloading encrypted media increases entropy without being ransomware.
- **How to Rectify:**
  - Combine entropy metrics with file rename counts and process parentage (e.g., checking if the writing process is signed or originating from a temporary folder).
