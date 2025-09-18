# ARC Task 082

def p(j):
    A = [k[:]for k in j]
    c, E = len(j), len(j[0])
    for k in range(E):
        if j[0][k]:
        for W in range(c):
        if W%2==0:A[W][k]=j[0][k]
        else:
        if k>0:A[W][k - 1]=j[0][k]
        if k<E - 1:A[W][k + 1]=j[0][k]
    return A
