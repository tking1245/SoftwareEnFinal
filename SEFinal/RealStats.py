import matplotlib
import pandas as pd
import csv
from bs4 import BeautifulSoup as bsp 
import requests
import matplotlib.pyplot as plt
import yfinance 

# Writing to CSV file
#with open('downData.csv', mode='w', newline='') as file:
#    writer = csv.writer(file)
#    writer.writerows(data)
#print("CSV file populated successfully!")

time_input = str(input()) # code to make the csv files named accordingly with respect to the timeframe being downloaded.

apple = yfinance.Ticker("AAPL")
data = apple.history(period = time_input)
df_data = pd.DataFrame(data) # convert the data to a dataFrame 

df_data.to_csv(time_input+".csv" , index = True) # 

print(data.head())



# temp code
def create_graph(t):

    t = str(input())

    apple = yfinance.Ticker("AAPL")
    data = apple.history(period = t)
    df_data = pd.DataFrame(data) # convert the data to a dataFrame 

    return (df_data.to_csv(t+".csv" , index = True))


