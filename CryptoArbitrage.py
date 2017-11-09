import requests
import matplotlib.pyplot as plt
import numpy
from twilio.rest import Client






client = Client(account_sid, auth_token)
i = 0
date = []
arbitrage = []

while (i<1):
    
    data = requests.get('https://localbitcoins.com/buy-bitcoins-online/COP/.json')

    if (data.status_code != 200):
        data = requests.get('https://localbitcoins.com/buy-bitcoins-online/COP/.json')
    COPprice = data.json()['data']['ad_list'][0]['data']['temp_price']

    USD2COP = 2923.8050

    BTC = requests.get('https://api.coinbase.com/v2/prices/BTC-USD/buy')

    if (BTC.status_code != 200):
       BTC = requests.get('https://api.coinbase.com/v2/prices/BTC-USD/buy')
       
    BTCoinbase = BTC.json()['data']['amount']

    t = requests.get('https://api.coinbase.com/v2/time')

    if (t.status_code != 200):
        t = requests.get('https://api.coinbase.com/v2/time')

    Time = t.json()['data']['epoch']

    iso = t.json()['data']['iso']

    Gain = round((( float(BTCoinbase)/(float(COPprice) / USD2COP) ) - 1)*100, 2)
    # To get date and time replace epoch with iso

    date.append(Time)

    
    arbitrage.append(Gain)
    
    plt.plot(date, arbitrage)
    plt.title("BTC Colombian Arbitrage")
    plt.ylabel("Profit % (USD $)")
    plt.xlabel("Time")
    plt.pause(1)
    plt.draw()
    
    if (Gain >= 10):
        client.messages.create(
            to = "+17866630320",
            from_= "+19548926238",
            body = "The Current BTC Arbitrage profit is " + str(Gain) + "% " + "That is a $" + str(round(float(BTCoinbase) - round((float(COPprice) / USD2COP),2),2)) + " discount...You should buy NOW!"
        )
        

    

    print("Current Time: " + str(iso))
    print("+++++++++++++++++++++++++++++++++++++++")
    print("+++++++++++++++++++++++++++++++++++++++")
    print("+++++++++++++++++++++++++++++++++++++++")
    print("+++++++++++++++++++++++++++++++++++++++")
    print("Current Coinbase Price: $" + BTCoinbase)
    print("+++++++++++++++++++++++++++++++++++++++")
    print("+++++++++++++++++++++++++++++++++++++++")
    print("Current Local Bitcoins Price: $" + str(round((float(COPprice) / USD2COP),2)))
    print("+++++++++++++++++++++++++++++++++++++++")
    print("Arbitrage gain: " + str(Gain) + "%" + "       A $" + str(round(float(BTCoinbase) - round((float(COPprice) / USD2COP),2),2)) + " Discount")
    print("+++++++++++++++++++++++++++++++++++++++")
    print("+++++++++++++++++++++++++++++++++++++++")
    print("+++++++++++++++++++++++++++++++++++++++")
    print("+++++++++++++++++++++++++++++++++++++++")

