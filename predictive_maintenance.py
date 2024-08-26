# src/predictive_maintenance.py
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import numpy as np

def build_lstm_model(input_shape):
    model = Sequential()
    model.add(LSTM(50, activation='relu', input_shape=input_shape))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mse')
    return model

def train_predictive_maintenance_model(data, labels):
    model = build_lstm_model((data.shape[1], data.shape[2]))
    model.fit(data, labels, epochs=50, batch_size=32, validation_split=0.2)
    return model

