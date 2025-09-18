# ARC Task 136

def p(j):
    A, c = len(j), len(j[0])
    E = lambda k:next((W, l)for W in range(A - 1)for l in range(c - 1)if j[W][l]==j[W + 1][l + 1]==k)
    W, l = E(1)
    while W>=1and l>=1:W, l = W - 1, l - 1
    j[W][l]=1
    W, l = E(2)
    while W<A - 1and l<c - 1:W, l = W + 1, l + 1
    j[W][l]=2
    return j
