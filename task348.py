# ARC Task 348

def p(j, A = range):
    c, E, k, W = len(j), len(j[0]), 0, 0
    for l in A(c):
    for J in A(E):
    if j[l][J]:k, W = l + 2, J
    def s(l, J, a):
    if 0<=J<E:j[l][J]=a
    for C in A(E):
    k, a = k - 1, 7 + C%2
    for l in A(k):s(l, W - C, a)
    s(l, W + C, a)
    return j
