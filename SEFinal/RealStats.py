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

s = input("Which stock would you like to investigate? \n please enter the stock name abreviation: ")
t = input("How far back in time would you like to investigate?\n Please use - 1mo, 3mo, 6mo, 1y, 3y, or all: ")


def create_graph(stock,time): # going to add s as a functional argument in order to control the stock being studied as well

    stock_name = yfinance.Ticker(str(stock))
    data = stock_name.history(period = str(time))
    df_data = pd.DataFrame(data) # convert the data to a dataFrame 

    return (df_data.to_csv(str(stock)+str(time)+".csv" , index = True))

create_graph(s,t)
