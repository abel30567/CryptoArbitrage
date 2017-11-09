import requests
import matplotlib.pyplot as plt
import numpy






i = 0
date = []
arbitrage = []

while (i<1):
    #################### LOCAL BITCOINS PERU ##################################
    data = requests.get('https://localbitcoins.com/buy-bitcoins-online/PEN/.json')

    if (data.status_code != 200):
        data = requests.get('https://localbitcoins.com/buy-bitcoins-online/PEN/.json')
    PENprice = data.json()['data']['ad_list'][0]['data']['temp_price']


    BTC = requests.get('https://localbitcoins.com/sell-bitcoins-online/PEN/national-bank-transfer/.json')

    if (BTC.status_code != 200):
       BTC = requests.get('https://localbitcoins.com/sell-bitcoins-online/PEN/national-bank-transfer/.json')
       
    PEN_BTC = BTC.json()['data']['ad_list'][0]['data']['temp_price_usd']

    USD2PEN = 3.1310
    ######################### COINBASE USA ########################
    BTC = requests.get('https://api.coinbase.com/v2/prices/BTC-USD/buy')

    if (BTC.status_code != 200):
       BTC = requests.get('https://api.coinbase.com/v2/prices/BTC-USD/buy')
       
    BTCoinbase = BTC.json()['data']['amount']

    time = requests.get('https://api.coinbase.com/v2/time')

    if (time.status_code != 200):
        time = requests.get('https://api.coinbase.com/v2/time')

    Time = time.json()['data']['epoch']

    iso = time.json()['data']['iso']

    Gain = (round((float(PENprice) / USD2PEN) / float(BTCoinbase), 3) - 1) * 100
    # To get date and time replace epoch with iso

    date.append(Time)

    
    arbitrage.append(Gain)
    
    plt.plot(date, arbitrage)
    plt.title("BTC Peruvian Arbitrage")
    plt.ylabel("Profit % (USD $)")
    plt.xlabel("Time")
    plt.pause(1)
    plt.draw()
    
    # if (Gain >= 400):
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
    print("Current Coinbase Price: $" + BTCoinbase)
    print("+++++++++++++++++++++++++++++++++++++++")
    print("+++++++++++++++++++++++++++++++++++++++")
    print("Current Local Bitcoins Price: $" + str(round((float(PENprice) / USD2PEN))))
    print("+++++++++++++++++++++++++++++++++++++++")
    print("Arbitrage gain: " + str(Gain) + "%")
    print("+++++++++++++++++++++++++++++++++++++++")
    print("+++++++++++++++++++++++++++++++++++++++")
    print("+++++++++++++++++++++++++++++++++++++++")
    print("+++++++++++++++++++++++++++++++++++++++")
