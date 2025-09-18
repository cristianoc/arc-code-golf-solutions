# ARC Task 139

from itertools import product
def p(j, A = range):
    for c, E in product(A(len(j)-2), A(len(j[0])-2)):
    k = A(c, c + 3)
    if not all(4 in i for i in[j[c][E:E + 3], j[c + 2][E:E + 3], [j[W][E]for W in k], [j[W][E + 2]for W in k]]):continue
    for W, l in product(k, A(E, E + 3)):j[W][l]+=7*(j[W][l]==0)
    return j
