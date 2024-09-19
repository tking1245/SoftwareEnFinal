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

# temp code
def create_graph(t,s): # going to add s as a functional argument in order to control the stock being studied as well

    stock_name = yfinance.Ticker(str(s))
    data = stock_name.history(period = str(t))
    df_data = pd.DataFrame(data) # convert the data to a dataFrame 

    return (df_data.to_csv(str(t)+".csv" , index = True))

create_graph(input(), input())
