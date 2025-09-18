# ARC Task 287

def p(g, L = len, R = range):
    h, w = L(g), L(g[0])
    for r in R(h//2 + 1):
    for c in R(w):
    if g[r][c]==4:g[r][c]=g[-(r + 1)][c]
    if g[-(r + 1)][c]==4:g[-(r + 1)][c]=g[r][c]
    for r in R(h):
    for c in R(w//2 + 1):
    if g[r][c]==4:g[r][c]=g[r][-(c + 1)]
    if g[r][-(c + 1)]==4:g[r][-(c + 1)]=g[r][c]
    return g
