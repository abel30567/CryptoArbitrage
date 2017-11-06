import requests


i = 0
date = []
arbitrage = []

while (i<1):
    
    data = requests.get('https://localbitcoins.com/buy-bitcoins-online/USD/.json')

    if (data.status_code != 200):
        data = requests.get('https://localbitcoins.com/buy-bitcoins-online/USD/.json')
    USDprice = data.json()['data']['ad_list'][0]['data']['temp_price']

    

    BTC = requests.get('https://localbitcoins.com/sell-bitcoins-online/GBP/national-bank-transfer/.json')

    if (BTC.status_code != 200):
       BTC = requests.get('https://localbitcoins.com/sell-bitcoins-online/GBP/national-bank-transfer/.json')
       
    GBP_BTC = BTC.json()['data']['ad_list'][0]['data']['temp_price_usd']

    time = requests.get('https://api.coinbase.com/v2/time')

    if (time.status_code != 200):
        time = requests.get('https://api.coinbase.com/v2/time')

    Time = time.json()['data']['epoch']
    iso = time.json()['data']['iso']
    # To get date and time replace epoch with iso

    date.append(Time)


    Gain = float(USDprice) - (float(GBP_BTC))
    arbitrage.append(Gain)

    
    print("Current Time: " + iso)
    print("+++++++++++++++++++++++++++++++++++++++")
    print("+++++++++++++++++++++++++++++++++++++++")
    print("+++++++++++++++++++++++++++++++++++++++")
    print("+++++++++++++++++++++++++++++++++++++++")
    print("Local Bitcoins Buy USD: " + USDprice)
    print("+++++++++++++++++++++++++++++++++++++++")
    print("+++++++++++++++++++++++++++++++++++++++")
    print("Local Bitcoins Sell GBP: " + GBP_BTC)
    print("+++++++++++++++++++++++++++++++++++++++")
    print("Arbitrage gain: " + str(Gain))
    print("+++++++++++++++++++++++++++++++++++++++")
    print("+++++++++++++++++++++++++++++++++++++++")
    print("+++++++++++++++++++++++++++++++++++++++")
    print("+++++++++++++++++++++++++++++++++++++++")


