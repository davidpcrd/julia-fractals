

def clamp(n):
    return min(255, max(0, n))

def gradient(x, rfactors, gfactors, bfactors):
    '''
    Return the r,g,b values along the predefined gradient for
    x in the range [0.0, 1.0].
    '''
    n = len(rfactors)
    r = clamp(int(sum(rfactors[i] * (x**(n-1-i)) for i in range(n))))
    g = clamp(int(sum(gfactors[i] * (x**(n-1-i)) for i in range(n))))
    b = clamp(int(sum(bfactors[i] * (x**(n-1-i)) for i in range(n))))
    return r, g, b
