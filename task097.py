# ARC Task 097

j = len
A = range
def p(c):
    E, k = j(c), j(c[0])
    W = [a for W in c for a in W]
    W = sorted(W)[-1]
    c = [[0]+W+[0]for W in c]
    l = [[0]*(k + 2)]
    c = l + c+l
    J = [[1, 1], [-1, -1], [-1, 1], [1, -1], [0, 1], [0, -1], [-1, 0], [1, 0], [0, 0]]
    for a in A(1, E + 1):
        for C in A(1, k + 1):
        if c[a][C]==W:
        e = [c[W[0]+a][W[1]+C]for W in J]
        if sum(e)==W:c[a][C]=0
    c = c[1:-1]
    c = [W[1:-1]for W in c]
    return c
