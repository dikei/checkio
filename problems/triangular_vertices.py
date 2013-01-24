from collections import defaultdict
import math
def checkio(param):
    """
    Solve the triangular vertices problem
    Based on algorithm described at:
    http://www.eecs.qmul.ac.uk/~pbo/ACM/archive/S00209.html
    """
    cord_map = {}
    row_map = {}
    max_size = max(param)
    for __i in range(1, max_size+1):
        row_map[__i] = math.ceil((2 * __i + 0.25) ** 0.5 - 0.5) - 1
        if (2 * (__i - 1) + 0.25) ** 0.5 - 0.5 == row_map[__i]:
            cord_map[__i] = (row_map[__i], 0)
        else:
            tmp = __i - row_map[__i] - 1
            x_cord = cord_map[tmp][0]
            y_cord = row_map[__i] - x_cord
            cord_map[__i] = (x_cord, y_cord)

    samex = len(set((cord_map[elem][0] for elem in param)))
    samey = len(set((cord_map[elem][1] for elem in param)))
    samerow = len(set((row_map[elem] for elem in param)))

    if len(param) == 3:
        if samex == 2 and samey == 2 and samerow == 2:
            return 3
    elif len(param) == 4:
        if ((samex == 2 and samey == 2 and samerow == 3) or
            (samex == 2 and samey == 3 and samerow == 2) or
            (samex == 3 and samey == 2 and samerow == 2)):
            return 4
    elif len(param) == 6:
        if samex == 3 and samey == 3 and samerow == 3:
            #Check for convex
            submap_x = defaultdict(int)
            submap_y = defaultdict(int)
            for elem in param:
                submap_x[cord_map[elem][0]] += 1
                if submap_x[cord_map[elem][0]] > 2:
                    return 0
                submap_y[cord_map[elem][1]] += 1
                if submap_y[cord_map[elem][1]] > 2:
                    return 0
            return 6
    return 0
