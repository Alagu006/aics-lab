"""
03_phishing_email_detection_manual.py - Phishing Email NLP Detection (CY3764 Manual)
REQUIRED PACKAGES:
  * pip install scikit-learn
  * Tested on: pip 26.1.2 | scikit-learn==1.9.1
"""
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

emails = [
    "URGENT: confirm card update security click link", "Your bank account has been suspended click here",
    "Claim $1,000,000 prize winning payout now", "Verify immediate password reset notification",
    "Quarterly department meeting scheduled for tomorrow", "Please find the attached lecture notes and slides",
    "Project status report and meeting agenda attached", "Your assignment submission deadline is Friday"
]
labels = [1, 1, 1, 1, 0, 0, 0, 0]  # 1: Phishing, 0: Legitimate

print(f"Loading dataset... Emails: {len(emails)} | Phishing: {sum(labels)} | Legitimate: {len(labels)-sum(labels)}")
model = make_pipeline(TfidfVectorizer(), MultinomialNB()).fit(emails, labels)

test_samples = [
    "Dear customer, your account has been suspended due to suspicious activity",
    "Hello Team, Please find the attached report for the quarterly review"
]
print("=" * 55 + "\nTESTING WITH NEW EMAILS\n" + "=" * 55)
for em in test_samples:
    pred, prob = model.predict([em])[0], model.predict_proba([em])[0]
    print(f"Email: {em[:50]}...\nPrediction: {'PHISHING' if pred else 'LEGITIMATE'} (Legitimate={prob[0]:.2f}, Phishing={prob[1]:.2f})\n")

"""
SAMPLE OUTPUT:
Loading dataset... Emails: 8 | Phishing: 4 | Legitimate: 4
=======================================================
TESTING WITH NEW EMAILS
=======================================================
Email: Dear customer, your account has been suspended du...
Prediction: PHISHING (Legitimate=0.34, Phishing=0.66)

Email: Hello Team, Please find the attached report for th...
Prediction: LEGITIMATE (Legitimate=0.72, Phishing=0.28)
"""
