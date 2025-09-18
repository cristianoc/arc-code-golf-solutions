# ARC Task 230

def p(j):
    A, c = len(j), len(j[0])
    for E in range(A - 1):
    for k in range(c - 1):
    if j[E][k]==j[E][k + 1]==j[E + 1][k]==j[E + 1][k + 1]==5:
    if E>0and k>0:j[E - 1][k - 1]=1
    if E>0and k + 2<c:j[E - 1][k + 2]=2
    if E + 2<A and k>0:j[E + 2][k - 1]=3
    if E + 2<A and k + 2<c:j[E + 2][k + 2]=4
    return j
