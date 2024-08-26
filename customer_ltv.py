# src/customer_ltv.py
from sklearn.ensemble import GradientBoostingRegressor
import pandas as pd

def train_ltv_model(data_path):
    data = pd.read_csv(data_path)
    X = data.drop(columns=['customer_id', 'ltv'])
    y = data['ltv']
    model = GradientBoostingRegressor()
    model.fit(X, y)
    return model

def predict_ltv(model, customer_data):
    return model.predict(customer_data)

