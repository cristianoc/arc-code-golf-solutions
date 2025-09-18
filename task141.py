# ARC Task 141

def p(j):
    A = [J[:]for J in j]
    c, E = len(j), len(j[0])
    for k in range(c):
        for W in range(E):
        if j[k][W]:
        l = j[k][W]
        for J in[(-1, -1), (-1, 1), (1, 1), (1, -1)]:
        a, C = k + J[0], W + J[1]
    while 0<=a<c and 0<=C<E:A[a][C]=l
    a+=J[0]
    C+=J[1]
    return A
