# Stock-Trend-Prediction
# Description
This project is an interactive Stock Trend Prediction application built using Streamlit for the frontend, LSTM (Long Short-Term Memory) Neural Networks using TensorFlow/Keras for time-series modeling, and pandas/matplotlib/NumPy for data processing and visualization.
The app allows users to input a stock ticker (e.g., AAPL, TSLA) and predict the future stock prices based on historical data (2010–2024).
![image alt](https://github.com/Manacydev/Stock-Trend-Prediction/blob/5a62fec6d36c9b25885f2e71a43e7708df03a770/image%201.png)
# Technologies Used
Python (Core language),
Streamlit (Web Application Framework),
TensorFlow (Keras) (Deep Learning Framework),
NumPy, pandas (Data Manipulation),
Matplotlib (Visualization),
Stooq API (Data Fetching) and
Jupyter Notebook (Model Building).
# Features
User Input for Stock Ticker.

Visualization:

Closing price vs Time

Moving Averages (100 MA and 200 MA)

Predicted vs Actual Stock Price.

Training LSTM Model dynamically.

Real-time Deployment using Streamlit
# Project Structure 
|-- Application/         # Streamlit Web Application
|-- STOCK.ipynb           # Colab Notebook for Data Preprocessing and Model Building
|-- app.py                # Streamlit App Script
|-- keras_model.keras     # Saved Trained Model (Keras format)
|-- requirements.txt      # Python libraries needed
|-- README.md             # Project Documentation
# Model Architecture
4-layer LSTM network with dropout layers.

Compiled using Adam Optimizer and Mean Squared Error loss.

Trained for 50 epochs.



