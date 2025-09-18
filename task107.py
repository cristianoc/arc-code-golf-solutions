# ARC Task 107

def p(j, u = range):
    A = len(j)
    c = len(j[0])
    E = len({*sum(j, [])}-{0})
    j = [[j[W//E][l//E]for l in u(c * E)]for W in u(A * E)]
    A*=E
    c*=E
    for k in u(min(A, c), 0, -1):
    for W in u(A - k + 1):
    for l in u(c - k + 1):
    J = j[W][l]
    if J and all(r[l:l + k]==[J]*k for r in j[W:W + k]):
    for a, C in(-1, -1), (-1, k), (k, -1), (k, k):
    e = W + a
    K = l + C
    while - 1<e<A and - 1<K<c and not j[e][K]:j[e][K]=2
    e+=a>0 or - 1
    K+=C>0 or - 1
    return j
