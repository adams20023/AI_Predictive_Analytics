# src/anomaly_detection.py
from sklearn.ensemble import IsolationForest
import pandas as pd
import numpy as np

def detect_anomalies(data_path, contamination=0.01):
    data = pd.read_csv(data_path)
    model = IsolationForest(contamination=contamination)
    model.fit(data)
    anomalies = model.predict(data)
    return anomalies

def auto_threshold_anomalies(data, threshold=1.5):
    data_mean = np.mean(data)
    data_std = np.std(data)
    anomalies = data[(data - data_mean) > threshold * data_std]
    return anomalies

