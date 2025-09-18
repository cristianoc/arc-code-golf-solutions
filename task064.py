# ARC Task 064

def p(g):
    I = [r[:] for r in g]
    H, W = len(I), len(I[0])
    vals = [v for r in I for v in r]
    bg = max(set(vals), key = vals.count)
    lc = min(sorted(set(vals)), key = vals.count)
    seen = [[False]*W for _ in range(H)]
    best = []
    for i in range(H):
        for j in range(W):
        if I[i][j]==bg or seen[i][j]:
        continue
        col = I[i][j]
        q = [(i, j)]
        comp = []
        seen[i][j]=True
        while q:
        a, b = q.pop()
        comp.append((a, b))
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        x, y = a + di, b + dj
        if 0<=x<H and 0<=y<W and not seen[x][y] and I[x][y]==col:
        seen[x][y]=True
        q.append((x, y))
        if len(comp)>len(best): best = comp
    L = [(i, j) for i in range(H) for j in range(W) if I[i][j]==lc]
    draw = set()
    for ai, aj in best:
        for bi, bj in L:
        if ai==bi:
        sj, ej = sorted((aj, bj))
        for j in range(sj, ej + 1): draw.add((ai, j))
        elif aj==bj:
        si, ei = sorted((ai, bi))
        for i2 in range(si, ei + 1): draw.add((i2, aj))
    for i, j in draw:
        if I[i][j]==bg: I[i][j]=lc
    return I
