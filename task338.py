# ARC Task 338

def p(j):
    A = range
    c = len(j)
    E = [[0]*c for B in A(c)]
    def B(k, W):
    if 0<=k<c and 0<=W<c and not E[k][W]and j[k][W]==0:E[k][W]=1
    [B(k + c, W + A)for(c, A)in[(1, 0), (-1, 0), (0, 1), (0, -1)]]
    [B(A, 0)or B(A, c - 1)or B(0, A)or B(c - 1, A)for A in A(c)]
    j = [[3 if j[B][c]==0and not E[B][c]else j[B][c]for c in A(c)]for B in A(c)]
    return[[3 if c==3 else 0 for c in r]for r in j]
