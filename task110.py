# ARC Task 110

def p(j, u = enumerate):
    A = range
    c = len(j)
    E = len(j[0])
    k = lambda W, l:W==l or W * l<1
    J = next((K for K in A(1, E)if all(k(L, e)for w in j for(L, e)in zip(w, w[K:]))), E)
    a = next((K for K in A(1, c)if all(k(L, e)for(K, w)in zip(j, j[K:])for(L, e)in zip(K, w))), c)
    C = {}
    for(e, K)in u(j):
        for(w, L)in u(K):
        if L:C[e%a, w%J]=L
    for(e, K)in u(j):
        for(w, L)in u(K):
        if not L:K[w]=C[e%a, w%J]
    return j
