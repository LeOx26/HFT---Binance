
from binance.client import Client
#Insert API and Secret key in quotation marks
class client():
 api_key = ''
 api_secret = ''
 client = Client(api_key, api_secret)

 candles = client.get_klines(symbol='BNBBTC', interval=Client.KLINE_INTERVAL_30MINUTE)
 candles
 print('edu')
