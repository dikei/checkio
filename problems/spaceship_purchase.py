__author__ = 'dikei'

def checkio(param):
    offer, raise_amt, price, drop_amt = param
    while True:
        offer += raise_amt
        if offer >= price:
            return price
        price -= drop_amt
        if offer >= price:
            return offer
