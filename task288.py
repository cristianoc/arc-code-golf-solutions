# ARC Task 288

from collections import Counter

def p(g):
    h, w = len(g), len(g[0])
    cnt = Counter(v for r in g for v in r)
    # Least frequent color
    least = min(cnt, key = cnt.get)
    # Coordinates of least color, shifted up by 1
    pts = [(i - 1, j) for i in range(h) for j in range(w) if g[i][j]==least]
    if not pts:
        return [row[:] for row in g]
    ti = min(i for i, j in pts)
    lj = min(j for i, j in pts)
    rj = max(j for i, j in pts)
    # Build diagonal rays from (ti, lj) to up - left; and from (ti, rj) to up - right
    rays = set()
    i, j = ti, lj
    while 0<=i<h and 0<=j<w:
        rays.add((i, j))
        i-=1
        j-=1
    i, j = ti, rj
    while 0<=i<h and 0<=j<w:
        rays.add((i, j))
        i-=1
        j+=1
    # Underfill: paint least color only over background cells
    bg = max(cnt, key = cnt.get)
    out = [row[:] for row in g]
    for i, j in rays:
        if 0<=i<h and 0<=j<w and out[i][j]==bg:
        out[i][j]=least
    return out
