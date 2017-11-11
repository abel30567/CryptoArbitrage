import requests
import matplotlib.pyplot as plt
import numpy
from twilio.rest import Client
import gdax
import time

public_client = gdax.PublicClient()



client = Client(account_sid, auth_token)
i = 0
date = []
arbitrage = []
start_time = time.time()


while (i<1):
    #########################BUY BTC IN COP #######################
    data = requests.get('https://localbitcoins.com/buy-bitcoins-online/COP/.json')

    if (data.status_code != 200):
        data = requests.get('https://localbitcoins.com/buy-bitcoins-online/COP/.json')
    
    USD2COP = 3100 # get the paypal API or site conversion api


    COP_BTC = float(data.json()['data']['ad_list'][0]['data']['temp_price'])/USD2COP + 5.00



     #########################SELL BTC IN USD GDAX#######################
    BTC = public_client.get_product_ticker(product_id='BTC-USD')

    USD_BTC = BTC['price']




    

    #####################PLOTTING############################
    t = BTC['time']

    Time = time.time() - start_time
    
    
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


    

    
    print("Current Time: " + t)
    print("+++++++++++++++++++++++++++++++++++++++")
    print("+++++++++++++++++++++++++++++++++++++++")
    print("+++++++++++++++++++++++++++++++++++++++")
    print("+++++++++++++++++++++++++++++++++++++++")
    print("Local Bitcoins Buy COP: " + str(COP_BTC))
    print("+++++++++++++++++++++++++++++++++++++++")
    print("+++++++++++++++++++++++++++++++++++++++")
    print("GDAX Sell USD: " + USD_BTC)
    print("+++++++++++++++++++++++++++++++++++++++")
    print("Arbitrage gain: " + str(Gain__per) + "%   that is a $" + str(round(Gain, 2)) + " Discount")
    print("+++++++++++++++++++++++++++++++++++++++")
    print("+++++++++++++++++++++++++++++++++++++++")
    print("+++++++++++++++++++++++++++++++++++++++")
    print("+++++++++++++++++++++++++++++++++++++++")


