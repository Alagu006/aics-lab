"""
06. Spam Detection
Purpose: Classify text messages as spam or legitimate using Naive Bayes.

REQUIRED PACKAGES:
  * pip install scikit-learn
  * Tested on: pip 26.1.2 | scikit-learn==1.9.1
"""
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

messages = [
    "Win cash now", "Claim your free prize",
    "Click here to win money", "Meeting at 10 am",
    "Please call me later", "Your class starts today"
]
labels = [1, 1, 1, 0, 0, 0]  # 1 = Spam, 0 = Legitimate

model = make_pipeline(CountVectorizer(), MultinomialNB())
model.fit(messages, labels)

samples = ["Claim prize click now", "Meeting at room 302"]
for s in samples:
    print(f"'{s}' -> {'[!] Spam' if model.predict([s])[0] else '[+] Not spam'}")

"""
SAMPLE OUTPUT:
'Claim prize click now' -> [!] Spam
'Meeting at room 302' -> [+] Not spam
"""
