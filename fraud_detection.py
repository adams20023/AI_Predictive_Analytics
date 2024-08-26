# src/fraud_detection.py
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np

def build_autoencoder(input_dim):
    model = Sequential()
    model.add(Dense(64, input_dim=input_dim, activation='relu'))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(input_dim, activation='sigmoid'))
    model.compile(optimizer='adam', loss='mse')
    return model

def train_fraud_detection_model(data):
    model = build_autoencoder(data.shape[1])
    model.fit(data, data, epochs=100, batch_size=32, validation_split=0.2)
    return model

