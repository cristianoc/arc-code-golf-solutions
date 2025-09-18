# ARC Task 027

from collections import Counter

def p(g):
    # Rotate 90° clockwise
    r = [list(t) for t in zip(*g[::-1])]
    h, w = len(g), len(g[0])
    hr, wr = len(r), len(r[0])

    # 1 - cells in original and rotated grids
    A = {(i, j) for i in range(h) for j in range(w) if g[i][j] == 1}
    B = {(i, j) for i in range(hr) for j in range(wr) if r[i][j] == 1}

    # Best offset aligning rotated 1s to original 1s
    best = None
    bs = -1
    offs = {(ai - bi, aj - bj) for ai, aj in A for bi, bj in B}
    for di, dj in offs:
        P = {(i + di, j + dj) for i, j in B}
        s = len(A & P)
        if s > bs:
        bs, best = s, P
        elif s == bs and best is not None:
        lj = min(j for i, j in P)
        bj = min(j for i, j in best)
        if lj < bj or (lj == bj and min(i for i, j in P) > min(i for i, j in best)):
        best = P

    # Underfill 2s under the chosen patch, without overwriting non - background
    cnt = Counter(v for row in g for v in row)
    bg = cnt.most_common(1)[0][0]
    o = [row[:] for row in g]
    if best:
        for i, j in best:
        if 0 <= i < h and 0 <= j < w and o[i][j] == bg:
        o[i][j] = 2
    return o
