import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as data
from sklearn.preprocessing import MinMaxScaler
import streamlit as st

start = '2010-01-01'
end = '2024-12-31'

st.title('Stock Trend Prediction')

user_input = st.text_input('Enter Stock Ticker', 'AAPL')
df = data.DataReader(user_input, 'stooq', start, end)
#describing data
st.subheader('Data from 2010 to 2024')
st.write(df.describe())
#Visualizations
st.subheader('Closing Price vs Time Chart')
fig=plt.figure(figsize=(12.6,7))
plt.plot(df.Close)
st.pyplot(fig)

st.subheader('Closing Price vs Time Chart with 100MA')
ma100=df.Close.rolling(100).mean()
fig1=plt.figure(figsize=(12.6,7))
plt.plot(ma100)
plt.plot(df.Close)
st.pyplot(fig1)

st.subheader('Closing Price vs Time Chart with 100MA and 200MA')
ma100=df.Close.rolling(100).mean()
ma200=df.Close.rolling(200).mean()
fig2=plt.figure(figsize=(12.6,7))
plt.plot(ma100, 'r')
plt.plot(ma200, 'g')
plt.plot(df.Close, 'b')
st.pyplot(fig2)

#from tensorflow.keras.models import load_model
data_training= pd.DataFrame(df['Close'][0:int(len(df)*0.70)])
data_testing= pd.DataFrame(df['Close'][int(len(df)*0.70):int(len(df))])
from sklearn.preprocessing import MinMaxScaler
scaler= MinMaxScaler(feature_range=(0,1))


scaler= MinMaxScaler(feature_range=(0,1))

data_training_array= scaler.fit_transform(data_training)
#splitting data into x_train and y_train
x_train=[] 
y_train=[]
for i in range(100,data_training_array.shape[0]): 
    x_train.append(data_training_array[i-100:i])
    y_train.append(data_training_array[i,0])

x_train, y_train = np.array(x_train), np.array(y_train)

from tensorflow.keras.models import load_model
model=load_model(r"C:\Users\HOME\Desktop\AI PROJECT\keras_model.keras")
# Save architecture
with open("config.json", "w") as json_file:
    json_file.write(model.to_json())

# Save weights
model.save_weights("model.weights.h5")
model.summary() 
#testing part
past_100_days = data_training.tail(100)
final_df = pd.concat([past_100_days, data_testing], ignore_index=True)
input_data=scaler.fit_transform(final_df)

x_test=[]
y_test=[]

for i in range(100,input_data.shape[0]):
    x_test.append(input_data[i-100:i])
    y_test.append(input_data[i,0])

x_test, y_test = np.array(x_test), np.array(y_test)

y_predicted = model.predict(x_test)
scaler=scaler.scale_

scale_factor= 1/scaler[0] #scaler will not be same for every stock
y_predicted= y_predicted * scale_factor
y_test=y_test*scale_factor

st.subheader('Predictions vs Original')
fig3=plt.figure(figsize=(12,6))
plt.plot(y_test, 'b', label='Original Price')
plt.plot(y_predicted, 'r', label='Predicted Price')
plt.xlabel('Time')
plt.ylabel('Price')
plt.legend()
plt.show() #as u can see predicted and test values r so nicely matching
st.pyplot(fig3)