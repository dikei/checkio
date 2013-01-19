def checkio(input):
    account, withdraws = input
    for amount in withdraws:
        if amount % 5:
            continue
        tmp = account - amount - 0.5 - amount * 0.01
        if tmp >= 0:
            account = int(tmp)
    return account
