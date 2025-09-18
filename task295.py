# ARC Task 295

def p(g, L = len, R = range):
    g = g[0]
    C = g[0]
    T = L([x for x in g if x>0])
    w = R(L(g))
    h = R(L(g)//2)
    X = [[0 for x in w] for y in h]
    for r in h:
    for c in w:
    if c<T:X[r][c]=C
    T+=1
    return X
