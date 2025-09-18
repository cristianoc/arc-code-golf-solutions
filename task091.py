# ARC Task 091

def p(j):
    A = len
    c = range
    E = []
    for k in c(A(j[0])):
        if any(j[c][k]==5 for c in c(A(j))):E.append(k)
    W = []
    for l in c(A(j)):
        if j[l][E[0]]==5:W.append(l)
    J, a = min(W)-1, max(W)+1
    C, e = E[0], E[1]
    return[[j[E][c]for c in c(C, e + 1)]for E in c(J, a + 1)]
