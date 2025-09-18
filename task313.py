# ARC Task 313

def p(g, r = range, l = len):
    n = l(g)
    q = l(set(g[0]))-1
    p = l({i[0]for i in g})-1
    for x in g:x[:]=(x[:q]*((l(x)-1)//q + 1))[:l(x)]
    for i in r(n):g[i]=[g[i%p][j]for j in r(n)]
    return[[dict(zip(g[0], g[0][1:]))[y]for y in r]for r in g]
