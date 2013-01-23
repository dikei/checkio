from collections import defaultdict

def checkio(param):
    cache = []
    #Scan each row and mark consecutive available position
    for line in param:
        counter = 0
        row = []
        for char in line:
            if char == 'G' or char == 'S':
                counter += 1
                row.append(counter)
            else:
                counter = 0
                row.append(0)
        cache.append(row)
    height = len(cache)
    width = len(cache[0])
    max_size = defaultdict(int)
    #Scan by column
    for __j in range(width):
        for __k in range(1, __j+2):
            __tmp = 0
            for __i in range(height):
                if cache[__i][__j] >= __k:
                    __tmp += 1
                else:
                    __tmp = 0
                #Find max area which have position index >= __k
                if __k * __tmp > max_size[__k]:
                    max_size[__k] = __k * __tmp
    return max(max_size.values())
