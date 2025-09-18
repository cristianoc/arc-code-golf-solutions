# ARC Task 009

def p(j, A = range, c = len):
    E = [J[:]for J in j]
    k, W = c(j), c(j[0])
    l = j[0][2]
    for J in A(k):
        for a in A(W):
    if j[J][a]==l:E[J][a]=l
    j[J][a]=0
        else:E[J][a]=0
    C = [J[:]for J in j]
    for e in A(k):
        K = [(J, a)for J in A(k)for a in A(W)if j[J][a]==e]
        for J in A(len(K)):
        for a in A(J + 1, len(K)):
    w, L = K[J]
    b, d = K[a]
        if w==b:
        for f in A(min(L, d), max(L, d)+1):C[w][f]=e
        elif L==d:
        for g in A(min(w, b), max(w, b)+1):C[g][L]=e
    for J in A(k):
        for a in A(W):
        if E[J][a]>0:C[J][a]=l
    return C
