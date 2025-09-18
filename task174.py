# ARC Task 174

def p(g):
    # Return the first 8‑connected non‑background unicolor object
    # whose cropped bounding box is horizontally symmetric.
    h, w = len(g), len(g[0])
    from collections import Counter, deque

    bg = Counter(v for r in g for v in r).most_common(1)[0][0]
    seen = [[False] * w for _ in range(h)]

    def bfs(si, sj):
        color = g[si][sj]
        q = deque([(si, sj)])
        seen[si][sj] = True
        cells = [(si, sj)]
        while q:
        i, j = q.popleft()
        for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
        if di == 0 and dj == 0:
        continue
        ni, nj = i + di, j + dj
        if 0 <= ni < h and 0 <= nj < w and not seen[ni][nj] and g[ni][nj] == color:
        seen[ni][nj] = True
        q.append((ni, nj))
        cells.append((ni, nj))
        return cells

    def crop(cells):
        is_ = [i for i, _ in cells]
        js_ = [j for _, j in cells]
        mi, ma = min(is_), max(is_)
        mj, mb = min(js_), max(js_)
        return [row[mj:mb + 1] for row in g[mi:ma + 1]]

    def is_horiz_sym(grid):
        return all(row == row[::-1] for row in grid)

    for i in range(h):
        for j in range(w):
        if g[i][j] != bg and not seen[i][j]:
        cells = bfs(i, j)
        cg = crop(cells)
        if is_horiz_sym(cg):
        return [list(r) for r in cg]

    # Fallback: return input unchanged
    return [list(row) for row in g]
