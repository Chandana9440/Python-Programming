import os
dic={} 
def secretBidAuction():
    name=input("Enter your name? ")
    bid=int(input("Enter your bid? $"))
    dic[name]=bid
    next_bid= input("Is there next person to bid: Yes/No? ")
    # Clearing the Screen
    os.system('cls')
    if next_bid=='Yes':
        secretBidAuction()
    else:
        highest_bid=0
        winner=''
        for key in dic:
            if dic[key]>highest_bid:
                highest_bid=dic[key]
                winner=key
            else:
                highest_bid=highest_bid
        print(f" The Winner {winner} has the highest bid of {highest_bid} ")
secretBidAuction()





