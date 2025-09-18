# ARC Task 359

def X(g):return list(zip(*g[::-1]))
def p(g, L = len, R = range):
    V = 0
    if max(g[0].count(i) for i in R(10))-1<L(g[0])/2:V = 1
    g = X(g)
    h, w = L(g), L(g[0])
    for r in R(h):
    C = sorted([[g[r].count(i), i] for i in R(10)])[-1][1]
    g[r]=[C]*w
    if V:g = X(X(X((g))))
    return [list(r) for r in g]
