# ARC Task 299

def p(g, L = len, R = range):
    h, w = L(g), L(g[0])
    for r in R(h):
    if g[r][0]==2 or g[r][-1]==2: 
    for c in R(w):
    if g[r][c]==0:g[r][c]=2
    elif g[r][c]!=2:g[r][c]=4
    for c in R(w):
    if g[0][c]==8 or g[-1][c]==8: 
    for r in R(h):
    if g[r][c]==0:g[r][c]=8
    elif g[r][c]!=8:g[r][c]=4
    return g
