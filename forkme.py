import requests
import matplotlib.pyplot as plt
import numpy
from twilio.rest import Client
import gdax
import time

public_client = gdax.PublicClient()

account_sid = "ACc5baa1da0a08f630ca8b547ee23823b7"
auth_token = "68ab65c4963f6e3392b2c74f88b493f6"

client = Client(account_sid, auth_token)
i = 0
date = []
BTC = list()
BitDiff = []
BCH = []
CashDiff = []
start_time = time.time()



while (i<1):
    #########################GET THE DARI DATA#######################
    dari = requests.get('https://api.fork.lol/')

    if (dari.status_code != 200):
        dari =  requests.get('https://api.fork.lol/')
    
    BCHdari = dari.json()['BCH']['history']['all'][256]['dari']
    BCHdiff = dari.json()['BCH']['history']['all'][256]['avg_diff']

    BTCdari = dari.json()['BTC']['history']['all'][256]['dari']
    BTCdiff = dari.json()['BTC']['history']['all'][256]['avg_diff']

    BTC.append(BTCdari)

    BitDiff.append(float(BTCdiff))

    BCH.append(float(BCHdari))
    CashDiff.append(float(BCHdiff))

    Time = time.time() - start_time

    date.append(Time)

    fig, ax = plt.subplots(2, sharex=True)
    ax[0].set_title('BTC vs BCH')
    ax[0].plot(date, BTC, 'r-', label = 'BTC DARI')
    ax[0].plot(date, BCH, 'b-', label = 'BCH DARI')
    ax[1].plot(date, BitDiff, 'r-', label = 'BTC Difficulty')
    ax[1].plot(date, CashDiff, 'b-', label = 'BCH Difficulty')
    plt.xlabel('Time')
    ax[0].legend(loc='upper center', shadow=True)
    ax[1].legend(loc='upper center', shadow=True)
    plt.pause(1)
    plt.draw()
    plt.close()