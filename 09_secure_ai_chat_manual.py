"""
09_secure_ai_chat_manual.py - Secure Chat AI Anomaly Detection Engine (CY3764 Manual)
REQUIRED PACKAGES:
  * pip install scikit-learn numpy
  * Tested on: pip 26.1.2 | scikit-learn==1.9.1 | numpy==2.2.4
"""
import hashlib, numpy as np
from sklearn.ensemble import IsolationForest

class SecureChatEngine:
    def __init__(self):
        self.users = {"alice": hashlib.sha256(b"secret123").hexdigest()}
        self.model = IsolationForest(contamination=0.05, random_state=42).fit(np.random.poisson(3, (200, 1)))
    def auth(self, u, p):
        return self.users.get(u) == hashlib.sha256(p.encode()).hexdigest()
    def check_rate(self, rate):
        return self.model.predict([[rate]])[0] == -1 or rate > 10

engine = SecureChatEngine()
print("=" * 55 + "\nSECURE CHAT APPLICATION WITH AI ANOMALY DETECTION\n" + "=" * 55)
print(f"Auth Test (Valid Creds)  : {'PASSED' if engine.auth('alice', 'secret123') else 'FAILED'}")
print(f"Auth Test (Invalid Creds): {'BLOCKED' if not engine.auth('alice', 'wrong') else 'ALLOWED'}")

print("\nMESSAGE VELOCITY ANOMALY TEST:")
for rate in [2, 5, 14, 25]:
    flag = engine.check_rate(rate)
    print(f"Rate: {rate:2d} msgs/min -> {'[!] ANOMALY FLAGGED (Potential Bot/Spam)' if flag else '[+] Normal Velocity'}")

"""
SAMPLE OUTPUT:
=======================================================
SECURE CHAT APPLICATION WITH AI ANOMALY DETECTION
=======================================================
Auth Test (Valid Creds)  : PASSED
Auth Test (Invalid Creds): BLOCKED

MESSAGE VELOCITY ANOMALY TEST:
Rate:  2 msgs/min -> [+] Normal Velocity
Rate:  5 msgs/min -> [+] Normal Velocity
Rate: 14 msgs/min -> [!] ANOMALY FLAGGED (Potential Bot/Spam)
Rate: 25 msgs/min -> [!] ANOMALY FLAGGED (Potential Bot/Spam)
"""
