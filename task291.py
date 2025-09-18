# ARC Task 291

def p(g, L = len, R = range):
    h, w = L(g), L(g[0])
    for r in R(h - 1):
    for c in R(w - 1):
    C = g[r][c:c + 2]+g[r + 1][c:c + 2]
    y = C.count(0)
    if y==1:
    for z in R(1, 10):
    if C.count(z)==3:return [[z]]
