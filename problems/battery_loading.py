def checkio(param):
    """
    Linear programming solution to battery loading problem
    """
    median = int(sum(param) / 2)
    size = len(param)
    mem = [[0 for j in range(median+1)] for i in range(size)]
    for i in range(0, size):
        for j in range(0, median+1):
            if param[i] > j:
                mem[i][j] = mem[i-1][j]
            else:
                mem[i][j] = max(mem[i-1][j], mem[i-1][j - param[i]] + param[i])
    return int(abs(sum(param) / 2 - mem[size-1][median]) * 2)
