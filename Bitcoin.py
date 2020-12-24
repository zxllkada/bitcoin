# Generator Bitcoin Wallets
import random

list = ['0','1','2','3','4','5','6','7','8','9','q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','Q','W','E','T','R','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']

wallets = []
wallet = 'bc'
for btcNum in range(1000):
    for btcGen in range(30):
        choosen = random.choice(list)
        wallet = wallet+choosen
        if btcGen == 29 :
            wallet = wallet+"*******"
            wallets.append(wallet)
            wallet = 'bc'
        else :
            pass
            
for WALLET in wallets :
    print (WALLET)



