from xmlrpc.client import ResponseError
import yfinance as yf
import pandas as pd 
import redis as r
from redis.commands.json.path import Path
import numpy as np
import time

global server
global date
server=r.Redis(host='localhost', port=6379, db=0)
dia=str(time.localtime().tm_mday)
mes=str(time.localtime().tm_mon-3)
year=str(time.localtime().tm_year)
date=year+'-'+mes+'-'+dia



class number():
  def __init__(self, number):
      self.number=number
  def numbers(self):
     if self.number<1000000: # cient mil
         num=str(self.number)
         mil='0.00000'+num
         return float(mil)
     elif self.number>=1000000 and self.number<10000000:# millon
          num=str(self.number)
          mil='0.0000'+num
          return float(mil)
     elif self.number>=10000000 and self.number<100000000: #diez millones
          num=str(self.number)
          mil='0.000'+num
          return float(mil)
     elif self.number>=100000000 and self.number<1000000000: #cien millones
          num=str(self.number)
          mil='0.00'+num
          return float(mil)
     elif self.number>=1000000000 and self.number<10000000000: #billon
          num=str(self.number)
          mil='0.0'+num
          return float(mil)
     elif self.number>=10000000000 and self.number<100000000000:#diez billon
          num=str(self.number)
          mil='0.'+num
          return float(mil)
     elif self.number>=100000000000 and self.number<1000000000000: #cien billon
          num=str(self.number)
          mil=num[0]+'.'+num[1:]
          return float(mil)
     elif  self.number>=1000000000000: #trillon
          num=str(self.number)
          mil=num[:2]+'.'+num[2:]
          return float(mil)


class set_server:
  def __init__(self,nombre=''):
        self.nombre=nombre
  def set_timeseries(self,value=None,timestamp=None,pandas_object=bool(),Dataframe=None):
     server.ts().create(key=self.nombre)
     if value is None:
        pass
     else:
        server.ts().add(self.nombre,timestamp=timestamp,value=value)
     if pandas_object is True:
          for i in range(Dataframe.values.size):
             server.ts().add(self.nombre,timestamp=str(Dataframe.index.values[i]),value=str(Dataframe.values[i]))
     print('guardado')
  def set_json (self,json_object):
      server.json().set(self.nombre,Path.root_path(),obj=json_object)
      print('guardado')

class save_data:
   def dat_stock_save(stock=''):
     shares=yf.Ticker(stock)
     info=shares.info
     price_table=shares.history(start=date)
     data_price=price_table['Close'].values
     pendiente=data_price[-1]-data_price[0]
     if pendiente>0:
       pdt=1
     else:
       pdt=0
     ganancias=info['totalRevenue']
     earning_per_share=info['revenuePerShare']
     flow=info['totalCash']
     debt=shares.info['debtToEquity']
     revenueGrowth=info['revenueGrowth']
     valor_contable=info['bookValue']
     data=pd.DataFrame(data={'tendencia':pdt,'ganancias':number(ganancias).numbers(),'earnisg_per_share':earning_per_share,'debtToEquity':debt,'grow Revenue':revenueGrowth,'flujo de caja':number(flow).numbers(),'valor contable':valor_contable},index=[stock])
     set_server(stock+"  "+"data_clustering_1").set_json(json_object=data.to_json())
   
   def load_market_all_data():
       with open('dataset/nasdaqlist11722.csv') as list:
          load=pd.read_csv(list)
       for i in range(load.size):
         for i in load.values[i]:
           stock=yf.Ticker(i).info

           try:
               stockType=stock['quoteType']
           except KeyError:
               pass
           if stockType=='EQUITY' :
                save_data.dat_stock_save(i)
           else:
                pass


       

       


  
   

    

    


      
     

     


