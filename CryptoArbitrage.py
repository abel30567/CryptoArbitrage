import requests
import matplotlib.pyplot as plt

i = 0
date = []
arbitrage = []

while (i<1):
    
    data = requests.get('https://localbitcoins.com/buy-bitcoins-online/COP/.json')

    if (data.status_code != 200):
        data = requests.get('https://localbitcoins.com/buy-bitcoins-online/COP/.json')
    COPprice = data.json()['data']['ad_list'][0]['data']['temp_price']

    USD2COP = 2947.20

    BTC = requests.get('https://api.coinbase.com/v2/prices/BTC-USD/buy')

    if (BTC.status_code != 200):
       BTC = requests.get('https://api.coinbase.com/v2/prices/BTC-USD/buy')
       
    BTCoinbase = BTC.json()['data']['amount']

    time = requests.get('https://api.coinbase.com/v2/time')

    if (time.status_code != 200):
        time = requests.get('https://api.coinbase.com/v2/time')

    Time = time.json()['data']['epoch']
    iso = time.json()['data']['iso']
    # To get date and time replace epoch with iso

    date.append(Time)
    
    sBTC = requests.get('https://api.coinbase.com/v2/prices/BTC-USD/sell')

    if (BTC.status_code != 200):
        sBTC = requests.get('https://api.coinbase.com/v2/prices/BTC-USD/sell')

    sBTCoinbase = sBTC.json()['data']['amount']


    Gain = float(BTCoinbase) - (float(COPprice) / USD2COP)
    arbitrage.append(Gain)

    plt.plot(date, arbitrage)
    plt.xlabel('Time')
    plt.ylabel('Profit')
    plt.title('BTC Arbitrage')  
    print("Current Time: " + iso)
    print("+++++++++++++++++++++++++++++++++++++++")
    print("+++++++++++++++++++++++++++++++++++++++")
    print("+++++++++++++++++++++++++++++++++++++++")
    print("+++++++++++++++++++++++++++++++++++++++")
    print("Coinbase price to buy: " + BTCoinbase)
    print("+++++++++++++++++++++++++++++++++++++++")
    print("Coinbase price to sell: " + sBTCoinbase)
    print("+++++++++++++++++++++++++++++++++++++++")
    print("Colombian cost: " + str((float(COPprice) / USD2COP)))
    print("+++++++++++++++++++++++++++++++++++++++")
    print("Arbitrage gain: " + str(Gain))
    print("+++++++++++++++++++++++++++++++++++++++")
    print("+++++++++++++++++++++++++++++++++++++++")
    print("+++++++++++++++++++++++++++++++++++++++")
    print("+++++++++++++++++++++++++++++++++++++++")


