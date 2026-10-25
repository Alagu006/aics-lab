"""
03. Phishing Email Detection
Purpose: Classify an email as phishing or legitimate using TF-IDF and Naive Bayes.

REQUIRED PACKAGES:
  * pip install scikit-learn
  * Tested on: pip 26.1.2 | scikit-learn==1.9.1
"""
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

emails = [
    "Win a free prize click now",
    "Urgent verify your bank account",
    "Claim your reward immediately",
    "Meeting scheduled for tomorrow",
    "Please find the class notes attached",
    "Your assignment deadline is Friday"
]
labels = [1, 1, 1, 0, 0, 0]  # 1 = Phishing, 0 = Legitimate

model = make_pipeline(TfidfVectorizer(), MultinomialNB())
model.fit(emails, labels)

# Test evaluation
test_emails = ["Urgent: verify your account password", "Please find class slides attached"]
for em in test_emails:
    pred = model.predict([em])[0]
    print(f"'{em}' -> {'[!] Phishing' if pred == 1 else '[+] Legitimate'}")

"""
SAMPLE OUTPUT:
'Urgent: verify your account password' -> [!] Phishing
'Please find class slides attached' -> [+] Legitimate
"""
