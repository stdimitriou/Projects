import urllib.request
import json
from time import sleep
def get_coin_data(coin):
    #url is broken dpwn into two pieces in order to find all the coins inside the dictionery
    url1="https://min-api.cryptocompare.com/data/pricemulti?fsyms="
    url2="&tsyms=EUR&e=CCCAGG"
    url=url1+coin+url2
    r=urllib.request.urlopen(url)
    html=r.read()
    html=html.decode()
    d=json.loads(html)
    return d[coin]["EUR"]

#reading file
with open("coin.txt")as f:
    data=f.read()
coin=json.loads(data)
#finding the coins names
keys=list(coin.keys())
i=len(keys)
print(i)
#coin amount
v=list(coin.values())
x=0
l=0
while x<=i-1:
    #checking the price
    k=get_coin_data(keys[x])
    print(k)
    #calculating the value of the amount that you input
    price=v[x]*k
    print(price)
    if x>i :
        break
    x=x+1
    #anti ip ban system
    sleep(5)
