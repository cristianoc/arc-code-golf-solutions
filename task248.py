# ARC Task 248

def p(j):
    A = [l[:]for l in j]
    c, E = len(j), len(j[0])
    k, W, l = c - 1, 0, 1
    while k>=0:
        A[k][W]=1
    if 0<=W + l<E:k-=1
    W+=l
    else:k-=1
    l = -l
    W+=l
    return A
