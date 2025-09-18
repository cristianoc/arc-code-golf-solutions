# ARC Task 214

def p(g, R = range):
    A = [[c for c in r[:3]] for r in g]
    C = [r[::-1]for r in A[::-1]]
    for r in R(3):
    for c in R(3):
    g[r][c + 4]=A[-(c + 1)][r]
    g[r][c + 8]=C[r][c]
    return g
