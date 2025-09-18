# ARC Task 143

from collections import Counter, deque

def p(g):
    h, w = len(g), len(g[0])
    # 3x3 top - left pattern of non - zero cells, normalized
    nz = {(i, j) for i in range(min(3, h)) for j in range(min(3, w)) if g[i][j]!=0}
    if not nz:
        return [row[:] for row in g]
    min_i = min(i for i, _ in nz)
    min_j = min(j for _, j in nz)
    pat = {(i - min_i, j - min_j) for i, j in nz}
    # Background color and 4 - connected objects of non - bg same - color pixels
    cnt = Counter(v for r in g for v in r)
    bg = max(cnt, key = cnt.get)
    out = [row[:] for row in g]
    seen = [[0]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
        if g[i][j]!=bg and not seen[i][j]:
        col = g[i][j]
        q = deque([(i, j)])
        seen[i][j]=1
        comp = []
        while q:
        x, y = q.popleft()
        comp.append((x, y))
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        u, v = x + dx, y + dy
        if 0<=u<h and 0<=v<w and not seen[u][v] and g[u][v]==col:
        seen[u][v]=1
        q.append((u, v))
        mi = min(x for x, _ in comp)
        mj = min(y for _, y in comp)
        shape = {(x - mi, y - mj) for x, y in comp}
        if shape==pat:
        for x, y in comp:
        out[x][y]=5
    # Overlay original 3x3 patch
    for i in range(min(3, h)):
        for j in range(min(3, w)):
        out[i][j]=g[i][j]
    return out
