# ARC Task 398

def p(g, L = len, R = range):
    s = R(L([x for x in set(g[0])if x>0])*5)
    X = [[0 for x in s]for y in s]
    g = g[0]
    T = 0
    for r in s:
    for c in R(5):
    try:X[-(r + 1)][c + T]=g[c]
    except:pass
    T+=1
    return X
