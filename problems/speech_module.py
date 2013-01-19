def checkio(number):
    converter = {
        1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
        6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
        11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
        15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
        19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty',
        50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty',
        90: 'ninety'
    }
    output = []

    hundredth = number // 100
    if hundredth in converter:
        output.append(converter[hundredth])
        output.append('hundred')

    remain = number % 100
    if remain in converter:
        output.append(converter[remain])
    else:
        tenth = remain // 10 * 10
        digit = remain % 10
        if tenth in converter:
            output.append(converter[tenth])
        if digit in converter:
            output.append(converter[digit])

    return ' '.join(output)
