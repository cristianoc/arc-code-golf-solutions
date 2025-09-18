# ARC Task 077

def p(g):
    I = [r[:] for r in g]
    H, W = len(I), len(I[0])
    # upscale by 2
    U = []
    for r in I:
        row = []
        for v in r:
        row+=([v]*2)
        U.extend([row[:], row[:]])
    UH, UW = len(U), len(U[0])
    # collect diag - connected objects of color 2
    seen = [[False]*UW for _ in range(UH)]
    objs = []
    for i in range(UH):
        for j in range(UW):
        if U[i][j]!=2 or seen[i][j]:
        continue
        q = [(i, j)]
        seen[i][j]=True
        cells = []
        while q:
        a, b = q.pop()
        cells.append((a, b))
        for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
        if di==dj==0: continue
        x, y = a + di, b + dj
        if 0<=x<UH and 0<=y<UW and not seen[x][y] and U[x][y]==2:
        seen[x][y]=True
        q.append((x, y))
        objs.append(cells)
    # preserve original color - 2 pixels
    keep2 = {(i, j) for i in range(UH) for j in range(UW) if U[i][j]==2}
    # helper
    def fill_rect(si, sj, ei, ej):
        for x in range(si, ei + 1):
        for y in range(sj, ej + 1):
        U[x][y]=4
    # self rectangles (backdrop minus object approximated by repainting 2s later)
    for a in objs:
        is_ = [i for i, _ in a]
        js = [j for _, j in a]
        fill_rect(min(is_), min(js), max(is_), max(js))
    # pairwise rectangles for pairs with min manhattan < 5
    def mindist(A, B):
        md = 10**9
        for ai, aj in A:
        for bi, bj in B:
        d = abs(ai - bi)+abs(aj - bj)
        if d<md: md = d
        if md==0: return 0
        return md
    n = len(objs)
    for i in range(n):
        for j in range(n):
        if mindist(objs[i], objs[j])<5:
        allc = objs[i]+objs[j]
        is_ = [x for x, _ in allc]
        js = [y for _, y in allc]
        fill_rect(min(is_), min(js), max(is_), max(js))
    # repaint color 2 over any 4s that covered objects
    for i, j in keep2:
        U[i][j]=2
    # downscale by 2 (take top - left sample)
    return [row[::2] for row in U[::2]]
