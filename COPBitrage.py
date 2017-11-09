import requests
import matplotlib.pyplot as plt
import numpy
from twilio.rest import Client


account_sid = "ACc5baa1da0a08f630ca8b547ee23823b7"
auth_token = "68ab65c4963f6e3392b2c74f88b493f6"

client = Client(account_sid, auth_token)
i = 0
date = []
arbitrage = []

while (i<1):
    #########################BUY BTC IN COP #######################
    data = requests.get('https://localbitcoins.com/buy-bitcoins-online/COP/.json')

    if (data.status_code != 200):
        data = requests.get('https://localbitcoins.com/buy-bitcoins-online/COP/.json')
    
    USD2COP = 2923.8050 # get the paypal API or site conversion api


    COP_BTC = float(data.json()['data']['ad_list'][0]['data']['temp_price'])/USD2COP



     #########################SELL BTC IN USD #######################
    BTC = requests.get('https://localbitcoins.com/sell-bitcoins-online/USD/national-bank-transfer/.json')
   
    if (BTC.status_code != 200):
       BTC = requests.get('https://localbitcoins.com/sell-bitcoins-online/USD/national-bank-transfer/.json')
       
    USD_BTC = BTC.json()['data']['ad_list'][0]['data']['temp_price_usd']




    

    #####################PLOTTING############################
    time = requests.get('https://api.coinbase.com/v2/time')

    if (time.status_code != 200):
        time = requests.get('https://api.coinbase.com/v2/time')

    Time = time.json()['data']['epoch']
    
    iso = time.json()['data']['iso']
    # To get date and time replace epoch with iso


    date.append(Time)
    
    Gain = float(USD_BTC) - (float(COP_BTC))
    Gain__per = round(((float(USD_BTC)/float(COP_BTC))-1)*100, 2)
    arbitrage.append(Gain__per)



    
    plt.plot(date, arbitrage)
    plt.title("BTC Colombian Arbitrage")
    plt.ylabel("Profit % (USD $)")
    plt.xlabel("Time")
    plt.pause(1)
    plt.draw()


    
    #######################TWILIO TEXT##########################
    if (Gain__per >= 10):
        client.messages.create(
            to = "+17866630320",
            from_= "+19548926238",
            body = "The Current BTC Arbitrage profit is " + str(Gain__per) + "% " + "That is a $" + str(round(Gain,2)) + " discount...You should buy NOW!"
        )


    

    
    print("Current Time: " + iso)
    print("+++++++++++++++++++++++++++++++++++++++")
    print("+++++++++++++++++++++++++++++++++++++++")
    print("+++++++++++++++++++++++++++++++++++++++")
    print("+++++++++++++++++++++++++++++++++++++++")
    print("Local Bitcoins Buy COP: " + str(COP_BTC))
    print("+++++++++++++++++++++++++++++++++++++++")
    print("+++++++++++++++++++++++++++++++++++++++")
    print("Local Bitcoins Sell USD: " + USD_BTC)
    print("+++++++++++++++++++++++++++++++++++++++")
    print("Arbitrage gain: " + str(Gain))
    print("+++++++++++++++++++++++++++++++++++++++")
    print("+++++++++++++++++++++++++++++++++++++++")
    print("+++++++++++++++++++++++++++++++++++++++")
    print("+++++++++++++++++++++++++++++++++++++++")


