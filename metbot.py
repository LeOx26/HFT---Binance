

from inspect import trace
from re import X
import MetaTrader5 as mt5
from matplotlib.pyplot import figimage, ticklabel_format, title
import numpy as np
from numpy.lib.function_base import append
import pandas as pd
from pandas._libs.tslibs import period
from pandas.tseries.offsets import Tick
from requests.models import Request 
import talib as tb
import plotly.graph_objects as px
import plotly.express as fig
import datetime as dt
import time

cuenta=64969399
contrasena='Eduardito51'
servidor='XMGlobal-MT5 2'


if not mt5.initialize(login=cuenta, server=servidor,password=contrasena):
    print("initialize() failed, error code =",mt5.last_error())
    quit()


hoy=dt.datetime.today()
hora_donde_comienza=hoy.hour
utc_from_Fr = dt.datetime(2021, 12, hoy.day,hoy.hour+7)
utc_from_t = dt.datetime(2022,2,hoy.day,hoy.hour+2)
def RSI(tm):
 ticks = mt5.copy_ticks_from("US100Cash", tm, 10000, mt5.COPY_TICKS_INFO)
 ticks_frame = pd.DataFrame(ticks)
 ticks_frame['time']=pd.to_datetime(ticks_frame['time'], unit='s')
 return ticks_frame['bid']
print(RSI(tm=utc_from_t)[-1:])



def Rsi_RATES(Time):
 rates = mt5.copy_rates_from("US100Cash", mt5.TIMEFRAME_M1,Time,500)
 rates_frame = pd.DataFrame(rates)
 rates_frame['time']=pd.to_datetime(rates_frame['time'], unit='s')
 frame=rates_frame['time']
 rates_frame['low'][-1:]=RSI(tm=utc_from_t)[-1:]
 low=rates_frame['low']
 
 rsi=tb.RSI(low,timeperiod=16)
 return rsi[-1:]-3
 
print(Rsi_RATES(Time=utc_from_Fr))



while hoy.hour<18:
 print(Rsi_RATES(Time=utc_from_Fr))
 
 if Rsi_RATES(Time=utc_from_Fr)>30:
    mt5.order_send(
     {
     "action": mt5.TRADE_ACTION_DEAL,
     "symbol": "US100Cash",
     "volume": 0.30,
     "type": mt5.ORDER_TYPE_SELL,
     "sl": 0,
     "tp": 400,
     "comment": "metbot abrio venta",
     "type_time": mt5.ORDER_TIME_GTC,
     "type_filling": mt5.ORDER_FILLING_RETURN,
    } ) 
    
 if Rsi_RATES(Time=utc_from_Fr)>30:
    mt5.order_send(
     {
     "action": mt5.TRADE_ACTION_DEAL,
     "symbol": "US100Cash",
     "volume": 0.30,
     "type": mt5.ORDER_TYPE_SELL,
     "sl": 0,
     "tp": 400,
     "comment": "metbot abrio venta",
     "type_time": mt5.ORDER_TIME_GTC,
     "type_filling": mt5.ORDER_FILLING_RETURN,
    } )

mt5.shutdown()




