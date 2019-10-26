import Pull

#Price to Miners' Revenue
btc_price = Pull.price['y']
btc_miners_revenue = Pull.revenue['y']
btc_miners_revenue_ratio =  btc_price/btc_miners_revenue
hashrate_revenue_ratio = Pull.hashrate['y']/Pull.revenue['y']
new_ratio = btc_miners_revenue_ratio/hashrate_revenue_ratio


#kWh Consumed
kwh_consumed = Pull.hashrate['y']/62*2790/1000*24

#Electricity Cost
elec_cost = kwh_consumed * 0.084

#Miner's gross profit
gross_profit = Pull.revenue['y'] - elec_cost

#Gross Profit Ratio
gp_ratio = gross_profit/Pull.price['y']

#print(gp_ratio)
gp_ratio_MA = gp_ratio.rolling(window=17).mean()

#Relative Price 50 Day Moving Averages
price_MA = Pull.price['y'].rolling(window=17).mean()
