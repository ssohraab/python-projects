def main():
    coke = 50

    while coke > 0:
        print("Amount Due:", coke)
        coin = get_coin(coke)
        coke = coke - coin

    if coke < 0:
        print("Change Owed:", 0-coke)
    else:
        print("Change Owed:",0)

def get_coin(coke):
    while True:
        coin = int(input("Insert Coin: "))
        if coin in (5,10,25):
            return coin
        else:
            print("Amount due:", coke)

main()