# ARC Task 331

def p(j, A = enumerate):
    c = []
    for E, k in A(j):
    for W, l in A(k):
    if j[E][W]==1:c+=[[E, W]]
    for J in c:
    a, C = J
    if a>0:j[a - 1][C]=2
    if a<9:j[a + 1][C]=8
    if C>0:j[a][C - 1]=7
    if C<9:j[a][C + 1]=6
    return j
