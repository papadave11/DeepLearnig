from pandas import read_csv
from datetime import datetime
from pandas import DataFrame
from pandas import concat
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from keras.models import Sequential
from keras.layers import Dense, LSTM
from keras.layers.core import Dense, Dropout, Activation
from keras.callbacks import EarlyStopping
import pandas as pd, numpy as np
from matplotlib import pyplot



# Python program to convert time
# from 12 hour to 24 hour format
# Function to convert the date format
def convert24(str1):
     
    # Checking if last two elements of time
    # is AM and first two elements are 12


    if str1[0] == "AM" and str1[0] == "12":
        return "00" + str1[1]
         
    # remove the AM    
    elif str1[0] == "AM":
        return str1[1]
     
    # Checking if last two elements of time
    # is PM and first two elements are 12   
    elif str1[0] == "PM" and str1[0] == "12":
        return str1[1]
         
    else:
         
        # add 12 to hours and remove PM
        return str(int(str1[1]) + 12)


dataset = read_csv('kumdan_2019.csv')
print(dataset.date[0])

dataset.date = convert24(dataset.date[0])
print(dataset.date)
print("ksksksks")

"""
print(dataset.hour[0])

#print(convert24("08:05:45 PM"))
"""