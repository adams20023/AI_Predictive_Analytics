# src/time_series_model.py
from prophet import Prophet
import pandas as pd

def train_forecasting_model(data_path):
    data = pd.read_csv(data_path)
    model = Prophet()
    model.fit(data)
    return model

def predict_future(model, periods):
    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)
    return forecast

