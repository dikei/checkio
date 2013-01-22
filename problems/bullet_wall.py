def checkio(param):
    """
    Based on the algorithm from this stackoverflow post
    http://stackoverflow.com/a/2932601/205528
    """
    w1, w2, a, b = param
    dx = w1[0] - a[0]
    dy = w1[1] - a[1]
    det = (w2[0] - w1[0]) * (b[1] - a[1]) - (w2[1] - w1[1]) * (b[0] - a[0])

    if det == 0:
        #4 point in a straight line
        if (w2[0] - a[0]) * (b[1] - a[1]) - (w2[1] - a[1]) * (b[0] - a[0]) == 0:
            #Check if B is between A and the segment
            if w1 < b < a or a < b < w1:
                return True
            return False
        else:
            return False
    else:
        u = (dy * (w2[0] - w1[0]) - dx * (w2[1] - w1[1])) / det
        v = (dy * (b[0] - a[0]) - dx * (b[1] - a[1])) / det
        #Check if two vector W1->W2 and A->B intersect
        if u > 0 and v > 0:
            interpoint = (a[0] + (b[0] - a[0]) * u,  a[1] + (b[1] - a[1]) * u)
            #Check if intersect point is in the segment
            if ((interpoint[0] - w2[0]) * (interpoint[0] - w1[0]) +
                (interpoint[1] - w2[1]) * (interpoint[1] - w1[1]) <= 0):
                return True
        return False
