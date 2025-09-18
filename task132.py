# ARC Task 132

def p(j, A = range, c = enumerate):
    E = len(j)
    k = len(j[0])
    W = [[0]*k for _ in A(E)]
    l = {v for G in j for v in G if v}
    for J in l:
    a = [b for b, G in c(j)for v in G if v==J]
    C = [d for b, G in c(j)for d, v in c(G)if v==J]
    e, K = min(a), max(a)+1
    w, L = min(C), max(C)+1
    for b in A(e, K):
    for d in A(w, L):W[b][d]=J
    return W
