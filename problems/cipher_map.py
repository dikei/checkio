def checkio(param):
    def key_transform(cipher_key):
        """
        Rotate matrix 90 degree
        """
        size = len(cipher_key)
        #Transpose
        for __j in range(size):
            for __i in range(__j):
                cipher_key[__i][__j], cipher_key[__j][__i] = \
                cipher_key[__j][__i], cipher_key[__i][__j]
        #Swap column
        for __i in range(size):
            for __j in range(size//2):
                cipher_key[__i][__j], cipher_key[__i][size - __j -1] = \
                cipher_key[__i][size - __j - 1], cipher_key[__i][__j]
        return cipher_key

    cipher_key, code_page = param
    cipher_key = [[char for char in row] for row in cipher_key]
    output = []
    for i in range(4):
        for __i, row in enumerate(cipher_key):
            for __j, char in enumerate(row):
                if char == 'X':
                    output.append(code_page[__i][__j])
        cipher_key = key_transform(cipher_key)
    return ''.join(output)
