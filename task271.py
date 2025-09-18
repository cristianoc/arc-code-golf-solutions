# ARC Task 271

def p(g, L = len, R = range):
    h, w = L(g), L(g[0])
    Z, z = [], 0
    for r in R(h - 2):
    for c in R(w - 2):
    C = g[r][c:c + 3]+g[r + 1][c:c + 3]+g[r + 2][c:c + 3]
    y = C.count(1)+(C.count(8)/10)
    if y>z:Z = C[:]
    z = y
    return [Z[:3], Z[3:6], Z[6:]]
