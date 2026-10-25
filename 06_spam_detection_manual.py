"""
06_spam_detection_manual.py - Spam Classification Comparison (CY3764 Manual)
REQUIRED PACKAGES:
  * pip install scikit-learn
  * Tested on: pip 26.1.2 | scikit-learn==1.9.1
"""
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score

texts = [
    "Win cash and gold coins now", "Claim your free mobile recharge instantly",
    "Exclusive prize money transfer available", "Urgent lottery winner claim today",
    "Staff meeting at 10 am in hall B", "Please submit your lab observation notebook",
    "Your semester exam timetable is published", "Let us discuss the project tomorrow"
]
labels = [1, 1, 1, 1, 0, 0, 0, 0]

nb = make_pipeline(TfidfVectorizer(), MultinomialNB()).fit(texts, labels)
svm = make_pipeline(TfidfVectorizer(), LinearSVC(random_state=42)).fit(texts, labels)

print("=" * 50 + "\nSPAM DETECTION RESULTS\n" + "=" * 50)
print(f"Naive Bayes Model Accuracy : {accuracy_score(labels, nb.predict(texts))*100:.2f}%")
print(f"Support Vector Machine (SVM): {accuracy_score(labels, svm.predict(texts))*100:.2f}%")

test_msg = "Claim your lottery prize voucher now"
pred = svm.predict([test_msg])[0]
print(f"\nTest Message: '{test_msg}'\nPrediction: {'[!] SPAM' if pred == 1 else '[+] LEGITIMATE'}")

"""
SAMPLE OUTPUT:
==================================================
SPAM DETECTION RESULTS
==================================================
Naive Bayes Model Accuracy : 100.00%
Support Vector Machine (SVM): 100.00%

Test Message: 'Claim your lottery prize voucher now'
Prediction: [!] SPAM
"""
