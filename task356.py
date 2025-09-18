# ARC Task 356

def p(j, A = range):
    c = [r[:]for r in j]
    for E in A(1, 10):
    k = [(W, l)for W in A(len(j))for l in A(len(j[0]))if j[W][l]==E]
    for W in A(len(k)):
    for l in A(W + 1, len(k)):
    J, a = k[W]
    C, e = k[l]
    if J==C:
    for K in A(min(a, e), max(a, e)+1):c[J][K]=E
    elif a==e:
    for w in A(min(J, C), max(J, C)+1):c[w][a]=E
    return c
