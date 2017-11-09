import requests
import matplotlib.pyplot as plt
import numpy






i = 0
date = []
arbitrage = []

while (i<1):
    
    data = requests.get('https://localbitcoins.com/buy-bitcoins-online/COP/.json')

    if (data.status_code != 200):
        data = requests.get('https://localbitcoins.com/buy-bitcoins-online/COP/.json')
    COPprice = data.json()['data']['ad_list'][0]['data']['temp_price']

    USD2COP = 2919.60

    BTC = requests.get('https://api.coinbase.com/v2/prices/BTC-USD/buy')

    if (BTC.status_code != 200):
       BTC = requests.get('https://api.coinbase.com/v2/prices/BTC-USD/buy')
       
    BTCoinbase = BTC.json()['data']['amount']

    time = requests.get('https://api.coinbase.com/v2/time')

    if (time.status_code != 200):
        time = requests.get('https://api.coinbase.com/v2/time')

    Time = time.json()['data']['epoch']

    iso = time.json()['data']['iso']

    Gain = float(BTCoinbase) - (float(COPprice) / USD2COP)
    # To get date and time replace epoch with iso

    date.append(Time)

    
    arbitrage.append(Gain)
    
    plt.plot(date, arbitrage)
    plt.title("BTC Colombian Arbitrage")
    plt.ylabel("Profit (USD $)")
    plt.xlabel("Time")
    plt.pause(1)
    plt.draw()
    
    # if (Gain >= 1000):
    #     client.messages.create(
    #         to = "+17866630320",
    #         from_= "+19548926238",
    #         body = "The Current BTC Arbitrage profit is $" + str(Gain) + " You should buy NOW!"
    #     )

     

    print("Current Time: " + str(iso))
    print("+++++++++++++++++++++++++++++++++++++++")
    print("+++++++++++++++++++++++++++++++++++++++")
    print("+++++++++++++++++++++++++++++++++++++++")
    print("+++++++++++++++++++++++++++++++++++++++")
    print("Current Coinbase Price: " + BTCoinbase)
    print("+++++++++++++++++++++++++++++++++++++++")
    print("+++++++++++++++++++++++++++++++++++++++")
    print("Current Local Bitcoins Price: " + str((float(COPprice) / USD2COP)))
    print("+++++++++++++++++++++++++++++++++++++++")
    print("Arbitrage gain: " + str(Gain))
    print("+++++++++++++++++++++++++++++++++++++++")
    print("+++++++++++++++++++++++++++++++++++++++")
    print("+++++++++++++++++++++++++++++++++++++++")
    print("+++++++++++++++++++++++++++++++++++++++")

