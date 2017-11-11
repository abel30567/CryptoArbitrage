Ex = 19700000 #COP -> BTC

USXOOM = 8478845 + 5634600 #Transfer 2995 + 2000

COPrate = 2948.87

ORICONT = round((Ex - USXOOM)/COPrate, 2) #  = 5586555
# At what exchange rate????????
fees = 10
totCost = ORICONT + 2000 + 2995 + fees

BTC_amount = 0.73864572 + 0.39282029

cost_rate = round(totCost/BTC_amount ,2)
print(cost_rate)