# ARC Task 161

def p(g, E = enumerate, R = range, L = len):
    h, w = L(g), L(g[0])
    d = {k:{0:[], 1:[]} for k in set(sum(g, []))}
    for(r, X)in E(g):
    for(c, C)in E(X):d[C][0]+=[r]
    d[C][1]+=[c]
    del d[0]
    C = sorted([[len(d[k][1])-(max(d[k][0])/100), k] for k in d])[0][1]
    g = [[c if c==C else 0 for c in r] for r in g]
    for r in R(h):
    if g[r][0]==C or g[r][-1]==C: 
    for c in R(w):g[r][c]=C
    for c in R(w):
    if g[0][c]==C or g[-1][c]==C: 
    for r in R(h):g[r][c]=C
    return g
