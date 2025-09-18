# ARC Task 328

def p(g):
    H, W = len(g), len(g[0])

    # Background color = most frequent value in grid
    flat = [v for r in g for v in r]
    bg = max(set(flat), key = flat.count)

    # Find 4 - connected, same - color objects excluding background
    vis = [[False] * W for _ in range(H)]
    objs = []  # list of (color, cells_list)
    for i in range(H):
        for j in range(W):
        if vis[i][j] or g[i][j] == bg:
        vis[i][j] = True
        continue
        col = g[i][j]
        stack = [(i, j)]
        vis[i][j] = True
        cells = []
        while stack:
        a, b = stack.pop()
        if g[a][b] != col:
        continue
        cells.append((a, b))
        if a > 0 and not vis[a - 1][b]:
        vis[a - 1][b] = True
        stack.append((a - 1, b))
        if a + 1 < H and not vis[a + 1][b]:
        vis[a + 1][b] = True
        stack.append((a + 1, b))
        if b > 0 and not vis[a][b - 1]:
        vis[a][b - 1] = True
        stack.append((a, b - 1))
        if b + 1 < W and not vis[a][b + 1]:
        vis[a][b + 1] = True
        stack.append((a, b + 1))
        if cells:
        objs.append((col, cells))

    # Compute centers as bounding - box centers (matching the DSL center())
    centers = []
    for _, cells in objs:
        mi = min(x for x, _ in cells)
        ma = max(x for x, _ in cells)
        mj = min(y for _, y in cells)
        mb = max(y for _, y in cells)
        ci = mi + (ma - mi + 1) // 2
        cj = mj + (mb - mj + 1) // 2
        centers.append((ci, cj))

    out = [row[:] for row in g]

    # Paint cells that are strictly closest (Manhattan) to an object's center
    # and have even Chebyshev distance to that center
    for i in range(H):
        for j in range(W):
        if not centers:
        continue
        dists = [abs(i - ci) + abs(j - cj) for (ci, cj) in centers]
        best = min(dists)
        if dists.count(best) != 1:
        continue  # not strictly closest (tie)
        k = dists.index(best)
        ci, cj = centers[k]
        cheb = max(abs(i - ci), abs(j - cj))
        if cheb % 2 == 0:
        out[i][j] = objs[k][0]

    return out
