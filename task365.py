# ARC Task 365

def p(j):
    A, c = len(j), len(j[0])
    E = -1
    for k in range(A):
        for W in range(c):
        if j[k][W]and(k<1 or j[k - 1][W]<1)and(W<1 or j[k][W - 1]<1):
        l = J=1
        while W + l<c and j[k][W + l]:l+=1
        while k + J<A and j[k + J][W]:J+=1
    a = [k[W:W + l]for k in j[k:k + J]]
    C = sum(k.count(2)for k in a)
    if C>E:E = C
    e = a
    return e
