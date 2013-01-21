import re

def checkio(param):
    lower_alpha = r'[a-z]+'
    upper_alpha = r'[A-Z]+'
    digit = r'[0-9]+'
    if len(param) < 10:
        return False
    if (re.search(lower_alpha, param) and
        re.search(upper_alpha, param) and
        re.search(digit, param)):
        return True
    return False
