from collections import Counter

def p(g):
    h,w=len(g),len(g[0])
    n=min(h,w)
    # Element-wise max between row i and column i (via transpose)
    out=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            out[i][j]=max(g[i][j], g[j][i])
    # Replace zeros with most common value in this grid
    cnt=Counter(v for r in out for v in r)
    common=max(cnt, key=cnt.get)
    for i in range(n):
        for j in range(n):
            if out[i][j]==0:
                out[i][j]=common
    # Paint main diagonal with value at (0,0)
    v=out[0][0]
    for k in range(n):
        out[k][k]=v
    return out

