import requests
import json
from pandas.io.json import json_normalize
import pandas as pd

#####GET HASHRATE DATA#####

#PULL BLOCKCHAIN.COM JSON
hashrate_raw = json.loads(requests.get("https://api.blockchain.info/charts/hash-rate?timespan=all&format=json").text)

#Normalize the JSON file to DataFrame
hashrate = json_normalize(hashrate_raw['values'])

#Convert UNIX time to readable dates
hashrate['x'] = pd.to_datetime(hashrate['x'], unit='s')
hashrate['x'] = hashrate['x'].dt.date





#####GET MINERS REVENUE DATA#####

#PULL BLOCKCHAIN.COM JSON
revenue_raw = json.loads(requests.get("https://api.blockchain.info/charts/miners-revenue?timespan=all&format=json").text)

#Normalize the JSON file to DataFrame
revenue = json_normalize(revenue_raw['values'])
#print(content)

#Convert UNIX time to readable dates
revenue['x'] = pd.to_datetime(revenue['x'], unit='s')





#####GET BTC MARKET PRICE DATA#####

#PULL BLOCKCHAIN.COM JSON
price_raw = json.loads(requests.get("https://api.blockchain.info/charts/market-price?timespan=all&format=json").text)

#Normalize the JSON file to DataFrame
price = json_normalize(price_raw['values'])
#print(content)

#Convert UNIX time to readable dates
price['x'] = pd.to_datetime(price['x'], unit='s')