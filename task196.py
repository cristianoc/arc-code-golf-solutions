# ARC Task 196

def p(j):
    A = range
    c, E = len(j), len(j[0])
    k = set()
    W = [e[:]for e in j]
    def M(l, J):
        if(l, J)in k or not(0<=l<c and 0<=J<E)or j[l][J]!=1:return[]
    k.add((l, J))
    return[(l, J)]+sum([M(l + e, J + A)for(e, A)in[(-1, 0), (1, 0), (0, -1), (0, 1)]], [])
    for a in A(c):
        for C in A(E):
        if j[a][C]==1 and(a, C)not in k:
    e = M(a, C)
    K, w, L, b = min(e[0]for e in e), max(e[0]for e in e), min(e[1]for e in e), max(e[1]for e in e)
        if len(e)==2*(w - K + b - L)and w>K and b>L and any(j[e][k]==0 for e in A(K + 1, w)for k in A(L + 1, b)):
        for(d, f)in e:W[d][f]=3
    return W
