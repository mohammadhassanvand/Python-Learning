amount_due = 50

while True:
    coin = int(input("Insert Coin: "))

    if coin in [25, 10, 5]:
        amount_due -= coin

    if amount_due > 0:
        print(f"Amount Due: {amount_due}")
    else:
        print(f"Change Owed: {-amount_due}")
        break