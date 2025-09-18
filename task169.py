# ARC Task 169

def p(j):
    A = range
    c = [L[:]for L in j]
    E = set()
    k = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for W in A(10):
        for l in A(10):
        if j[W][l]==5 and(W, l)not in E:
    J, a = set(), [(W, l)]
    J.add((W, l))
    E.add((W, l))
        while a:
        C, e = a.pop(0)
        for(K, w)in k:
        L, b = C + K, e + w
    if 0<=L<10 and 0<=b<10 and j[L][b]==5 and(L, b)not in J:J.add((L, b))
    E.add((L, b))
    a.append((L, b))
        d = 5 - len(J)
        for(C, e)in J:c[C][e]=d
    return c
