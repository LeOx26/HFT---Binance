


import time as tm
import pandas as pd
from streamlit.elements.arrow import Data
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import streamlit as st
def stock_frames(symbol):
 
 tick=yf.Ticker(symbol)
 stock=tick.history(period="1mo",interval='1m',start="2022-2-3")
 return stock
 
fig=stock_frames('BTC-USD')['Low'][stock_frames('BTC-USD')['Low'].size-1:]


#last_rows =fig
#chart = st.line_chart(last_rows)

#for i in range(1, 100000):
    #new_rows =stock_frames('ETH-USD')['Low']
    
    #chart.add_rows(new_rows)
    
    #last_rows = new_rows
    #st.write(stock_frames('ETH-USD')['Low'][stock_frames('ETH-USD')['Low'].size-1:])

    #tm.sleep(30)



last_rows =stock_frames('BTC-USD')['Low'][stock_frames('BTC-USD')['Low'].size-1:].values
chart = st.line_chart(last_rows)

for i in range(1, 101):
    new_rows =stock_frames('ETH-USD')['Low'][stock_frames('ETH-USD')['Low'].size-1:].values
    
    chart.add_rows(new_rows)
    
    last_rows = new_rows
    tm.sleep(30)



    







