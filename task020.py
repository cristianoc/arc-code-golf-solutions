# ARC Task 020

def p(g, H = enumerate):
    t = l=9**9
    b = r=-1
    for y, a in H(g):
    for x, v in H(a):
    if v:t = min(t, y)
    b = max(b, y)
    l = min(l, x)
    r = max(r, x)
    s = t + b
    S = l + r
    for y in range(t, b + 1):
    for x in range(l, r + 1):
    Y = s - y
    X = S - x
    u = t + x - l
    v = l + y - t
    U = t + r - x
    V = l + b - y
    P = ((y, x), (y, X), (Y, x), (Y, X), (u, v), (U, v), (u, V), (U, V))
    c = max(g[i][j]for i, j in P)
    for i, j in P:g[i][j]=c
    return g
