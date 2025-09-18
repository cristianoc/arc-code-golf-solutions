# ARC Task 070

def p(j):
    A = range
    c = [E[:]for E in j]
    E = [(E, c)for E in A(len(j))for c in A(len(j[0]))if j[E][c]==8]
    if E:
    k, W = min(E for(E, A)in E), max(E for(E, A)in E)
    l, J = min(E for(A, E)in E), max(E for(A, E)in E)
        for a in A(k, W + 1):
        for C in A(l, J + 1):
        if j[a][C]==1:c[a][C]=3
    return c
