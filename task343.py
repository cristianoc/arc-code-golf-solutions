# ARC Task 343

def solve_d8c310e9(I):
    # Repeat the unique non - background motif horizontally with its column period
    G = [row[:] for row in I]
    H, W = len(G), len(G[0])

    # Background is most frequent color
    from collections import Counter
    flat = [v for r in G for v in r]
    bg = Counter(flat).most_common(1)[0][0]

    # Find first non - bg cell and collect its 4 - connected component (ignoring color)
    def bfs(si, sj):
        q = [(si, sj)]
        seen = {(si, sj)}
        cells = []  # (i, j, color)
        while q:
        i, j = q.pop()
        cells.append((i, j, G[i][j]))
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        ni, nj = i + di, j + dj
        if 0 <= ni < H and 0 <= nj < W and (ni, nj) not in seen and G[ni][nj] != bg:
        seen.add((ni, nj))
        q.append((ni, nj))
        return cells

    start = None
    for i in range(H):
        for j in range(W):
        if G[i][j] != bg:
        start = (i, j)
        break
        if start:
        break
    if not start:
        return [row[:] for row in I]

    obj = bfs(*start)
    min_i = min(i for i, j, _ in obj)
    min_j = min(j for i, j, _ in obj)
    # Build column signatures of normalized object: map col -> sorted[(row_offset, color)]
    cols = {}
    for i, j, c in obj:
        cols.setdefault(j - min_j, []).append((i - min_i, c))
    for k in cols:
        cols[k].sort()
        cols[k] = tuple(cols[k])
    width = max(cols) + 1

    # Find minimal horizontal period p
    def sig(j):
        return cols.get(j, tuple())
    p = width
    for cand in range(1, width + 1):
        ok = True
        for jj in range(0, width - cand):
        if sig(jj) != sig(jj + cand):
        ok = False
        break
        if ok:
        p = cand
        break

    # Paint copies of the motif every p columns to the right
    for i, j, c in obj:
        base_off = j - min_j
        for mul in range(0, (W - min_j + p - 1) // p + 1):
        nj = min_j + base_off + mul * p
        if 0 <= nj < W:
        G[i][nj] = c

    return G

def p(g):
    return solve_d8c310e9([row[:] for row in g])
