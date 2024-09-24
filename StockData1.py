import yfinance as yf

ticker = input ("Enter The Ticker : ")
from_data = input ("Enter The Start date (YYYY-MM-DD): ")
to_data = input("Enter The End Data (YYYY-MM-DD): ")

stock_data = yf.download(ticker,start = from_data, end = to_data)
stock_data.to_csv("Stock_Data.csv")
print("Stock data written to Stock_data.csv")