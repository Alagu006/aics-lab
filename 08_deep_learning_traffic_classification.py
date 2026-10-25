"""
08. Network Traffic Classification Using Deep Learning
Purpose: Classify traffic into Normal (0), DoS (1), and PortScan (2).

REQUIRED PACKAGES:
  * pip install tensorflow scikit-learn numpy
  * Tested on: pip 26.1.2 | scikit-learn==1.9.1 | numpy==2.2.4 | tensorflow >= 2.12.0
"""
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Simulated traffic: 0 = Normal, 1 = DoS, 2 = PortScan
rng = np.random.default_rng(4)
X = np.vstack([
    rng.normal([30, 10], 5, (100, 2)),    # Normal
    rng.normal([200, 80], 15, (100, 2)),  # DoS
    rng.normal([80, 150], 10, (100, 2))   # PortScan
])
y = np.repeat([0, 1, 2], 100)

Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=1, stratify=y)
scaler = StandardScaler()
Xtr, Xte = scaler.fit_transform(Xtr), scaler.transform(Xte)
classes = ["Normal", "DoS", "PortScan"]

try:
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Dense, Input

    model = Sequential([
        Input(shape=(2,)),
        Dense(16, activation="relu"),
        Dense(8, activation="relu"),
        Dense(3, activation="softmax")
    ])
    model.compile("adam", "sparse_categorical_crossentropy", metrics=["accuracy"])
    model.fit(Xtr, ytr, epochs=10, verbose=0)
    print(f"Accuracy: {model.evaluate(Xte, yte, verbose=0)[1] * 100:.1f}%")
    pred = model.predict(scaler.transform([[200, 80]]), verbose=0).argmax()
    print(f"Sample [200, 80] -> Predicted: {classes[pred]}")
except ImportError:
    from sklearn.neural_network import MLPClassifier
    mlp = MLPClassifier(hidden_layer_sizes=(16, 8), max_iter=200, random_state=1).fit(Xtr, ytr)
    pred = mlp.predict(scaler.transform([[200, 80]]))[0]
    print(f"[Fallback MLP] Accuracy: {mlp.score(Xte, yte)*100:.1f}% | Predicted: {classes[pred]}")

"""
SAMPLE OUTPUT:
[Fallback MLP] Accuracy: 100.0% | Predicted: DoS
"""
