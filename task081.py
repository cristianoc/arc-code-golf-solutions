# ARC Task 081

from collections import*
def p(j, A = range):
    c = [[8 if J==8 else 0 for J in R]for R in j]
    for E in A(len(j)-1):
        for k in A(len(j[0])-1):
    W = [j[E][k:k + 2], j[E + 1][k:k + 2]]
    l = [x for R in W for x in R]
    J = Counter(l).most_common(1)
        if J[0][1]==3and J[0][0]!=0:
        for a in A(E, E + 2):
        for C in A(k, k + 2):
        if c[a][C]==0:c[a][C]=1
    return c
