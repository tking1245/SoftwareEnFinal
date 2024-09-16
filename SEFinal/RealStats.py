import matplotlib
import pandas as pd
import csv
from bs4 import BeautifulSoup as bsp 
import requests
import matplotlib.pyplot as plt
import yfinance 

apple_stock = yfinance.Ticker("AAPL")
apple_data = apple_stock.history("6mo")



aFrame = pd.DataFrame.to_markdown(apple_data)
print(aFrame)
