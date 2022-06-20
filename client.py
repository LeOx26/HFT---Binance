
from binance.client import Client
#Insert API and Secret key in quotation marks
class client():
 api_key = 'kr41YsYIbL19a44v3vjifmD2vm6B0nldyQE6GQ7ulShpNpP4GdHU3Yl25Tr82TgO'
 api_secret = 'TbqgIWkv45W42MDkW2cs1GYwhZGRteIBf38SeVKym85OnrszPalUyY16S7CjiO32'
 client = Client(api_key, api_secret)

 candles = client.get_klines(symbol='BNBBTC', interval=Client.KLINE_INTERVAL_30MINUTE)
 candles
 print('edu')