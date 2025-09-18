# ARC Task 396

def p(j):
    A = range
    c, E = len(j), len(j[0])
    k = {}
    for W in A(c):
        for l in A(E):
        if j[W][l]:k[j[W][l]]=k.get(j[W][l], 0)+1
    J, a = max(k, key = k.get), min(k, key = k.get)
    C, e = 0, None
    for K in A(c - 2):
        for w in A(E - 2):
        for L in A(K + 2, c):
        for b in A(w + 2, E):
        if all(j[K][A]==J for A in A(w, b + 1))and all(j[L][A]==J for A in A(w, b + 1))and all(j[A][w]==J for A in A(K, L + 1))and all(j[A][b]==J for A in A(K, L + 1)):
        d = (L - K + 1)*(b - w + 1)
        if d>C:C, e = d, (K, w, L, b)
    K, w, L, b = e
    return[[a if j[K + L][w + A]==J else j[K + L][w + A]for A in A(b - w + 1)]for L in A(L - K + 1)]
