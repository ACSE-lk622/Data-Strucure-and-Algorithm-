def coinchange(totalnumber,coins):
    N = totalnumber
    coins.sort()
    index = len(coins)-1
    while True: #O(N)
        coinvalue = coins[index]
        if N >= coinvalue:
            print(coinvalue)
            N = N - coinvalue
        if N < coinvalue:
            index -= 1
        if N == 0 :
            break 

coin = [1,2,5,20,50,100]

coinchange(201,coin)