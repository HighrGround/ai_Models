import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error
import streamlit as st
import tensorflow as tf

# Collect and preprocess data
df = pd.read_csv('/Users/nathancassells/Downloads/CryptocurrencyPricesDataset.csv')
df.values
#df['date'] = pd.to_datetime(df['date'])
#df = df.set_index('date')

# Split data into training and testing sets
#train_df, test_df = train_test_split(df, test_size=0.2)

# Train the model
#regressor = LinearRegression()
#regressor.fit(train_df['past_prices'].values.reshape(-1, 1), train_df['future_prices'].values.reshape(-1, 1))

# Evaluate the model
#predictions = regressor.predict(test_df['past_prices'].values.reshape(-1, 1))
#mae = mean_absolute_error(test_df['future_prices'].values, predictions)
#mse = mean_squared_error(test_df['future_prices'].values, predictions)

# Make predictions
#future_prices = regressor.predict(df['past_prices'].values.reshape(-1, 1))
