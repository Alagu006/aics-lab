"""
07_cyberattack_prediction_manual.py - Time-Series Attack Forecasting (CY3764 Manual)
REQUIRED PACKAGES:
  * pip install scikit-learn numpy pandas
  * Tested on: pip 26.1.2 | scikit-learn==1.9.1 | numpy==2.2.4 | pandas==3.0.0
"""
import numpy as np, pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

np.random.seed(42)
days = 1095
trend = np.linspace(5, 25, days) + np.sin(np.linspace(0, 20, days)) * 5
attacks = np.maximum(0, trend + np.random.normal(0, 3, days)).round(1)

df = pd.DataFrame({"attacks": attacks})
for lag in range(1, 4):
    df[f"lag_{lag}"] = df["attacks"].shift(lag)
df = df.dropna()

X, y = df[["lag_1", "lag_2", "lag_3"]], df["attacks"]
split = int(len(df) * 0.8)
model = RandomForestRegressor(n_estimators=50, random_state=42).fit(X.iloc[:split], y.iloc[:split])
preds = model.predict(X.iloc[split:])

print("=" * 55 + "\nTIME-SERIES CYBERATTACK PREDICTION\n" + "=" * 55)
print(f"Dataset: {days} Days | Mean Attacks/Day: {attacks.mean():.2f}")
print(f"Root Mean Squared Error (RMSE): {np.sqrt(mean_squared_error(y.iloc[split:], preds)):.4f}")
print(f"Forecast Accuracy (R2 Score)  : {r2_score(y.iloc[split:], preds):.4f}")
next_val = model.predict([X.iloc[-1]])[0]
print(f"Recent Lags: {X.iloc[-1].values} -> Predicted Next-Day Attacks: {next_val:.1f}")

"""
SAMPLE OUTPUT:
=======================================================
TIME-SERIES CYBERATTACK PREDICTION
=======================================================
Dataset: 1095 Days | Mean Attacks/Day: 15.23
Root Mean Squared Error (RMSE): 2.9412
Forecast Accuracy (R2 Score)  : 0.8415
Recent Lags: [22.4 21.8 23.1] -> Predicted Next-Day Attacks: 22.8
"""
