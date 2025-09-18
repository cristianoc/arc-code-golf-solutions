# ARC Task 302

def p(j):
    A, c = len(j), len(j[0])
    E = [[0]*c for b in j]
    k = []
    def e(W, l):
    J = [(W, l)]
    E[W][l]=1
    a = [(W, l)]
    C = 1
        while J:
        e, K = J.pop()
        for(w, L)in[(0, 1), (1, 0), (0, -1), (-1, 0)]:
        b, k = e + w, K + L
    if not(0<=b<A and 0<=k<c):C = 0
    continue
    if j[b][k]<1 and not E[b][k]:E[b][k]=1
    J+=[(b, k)]
    a+=[(b, k)]
        return a if C else[]
    for b in range(A):
        for J in range(c - 1, -1, -1):
        if j[b][J]<1 and not E[b][J]:k+=[e(b, J)]
    k.sort(key = len, reverse = 1)
    for(b, a)in enumerate(k):
        K = min(8, max(6, len(a)**.5+.0 + 5))
        for C in a:j[C[0]][C[1]]=K
    return j
