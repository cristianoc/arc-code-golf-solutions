# ARC Task 237

def p(g, L = len, R = range):
    h, w = len(g), len(g[0])
    for r in R(h):
    s = 0
    for c in R(w):
    if g[-(r + 1)][c]>0:s = g[-(r + 1)][c]
    g[-(r + 1)][c]=s
    s = 0
    for r in R(h):
    if g[r][-1]>0:s = g[r][-1]
    g[r][-1]=s
    return g
