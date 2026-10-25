"""
07. Cyberattack Prediction Using Time-Series Analysis
Purpose: Predict attack activity in the next time interval using lagged features.

REQUIRED PACKAGES:
  * pip install pandas scikit-learn numpy
  * Tested on: pip 26.1.2 | pandas==3.0.0 | scikit-learn==1.9.1 | numpy==2.2.4
"""
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

rng = np.random.default_rng(3)
attack = rng.binomial(1, 0.15, 300)
for i in range(1, len(attack)):
    if attack[i - 1] and rng.random() < 0.7:
        attack[i] = 1

df = pd.DataFrame({"attack": attack})
for lag in [1, 2, 3]:
    df[f"lag{lag}"] = df["attack"].shift(lag)
df["target"] = df["attack"].shift(-1)
df = df.dropna()

X = df[["lag1", "lag2", "lag3"]]
y = df["target"].astype(int)
split = int(len(df) * 0.8)

model = RandomForestClassifier(random_state=1)
model.fit(X.iloc[:split], y.iloc[:split])

pred = model.predict(X.iloc[[-1]])[0]
print(f"Recent Lags: {X.iloc[-1].to_dict()}")
print(f"Next-Interval Prediction: {'[!] Attack Expected (1)' if pred == 1 else '[+] Normal (0)'}")

"""
SAMPLE OUTPUT:
Recent Lags: {'lag1': 0.0, 'lag2': 0.0, 'lag3': 0.0}
Next-Interval Prediction: [+] Normal (0)
"""
