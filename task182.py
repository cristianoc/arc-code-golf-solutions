# ARC Task 182

def p(g):
    # Compact solution for 776ffc46:
    # - Find the 4 - connected lime (5) rectangular frame object.
    # - Take one - cell inset region, gather the non - zero pattern and its color.
    # - Recolor every non - background object whose normalized shape matches that pattern.
    from collections import Counter, deque

    h, w = len(g), len(g[0])
    bg = Counter(v for r in g for v in r).most_common(1)[0][0]

    def bfs4(si, sj):
        color = g[si][sj]
        q = deque([(si, sj)])
        seen = {(si, sj)}
        cells = [(si, sj)]
        while q:
        i, j = q.popleft()
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        ni, nj = i + di, j + dj
        if 0 <= ni < h and 0 <= nj < w and (ni, nj) not in seen and g[ni][nj] == color:
        seen.add((ni, nj))
        q.append((ni, nj))
        cells.append((ni, nj))
        return color, cells

    visited = [[False] * w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
        if g[i][j] != bg and not visited[i][j]:
        color, cells = bfs4(i, j)
        for ci, cj in cells:
        visited[ci][cj] = True
        comps.append((color, cells))

    def bbox(cells):
        is_ = [i for i, _ in cells]
        js_ = [j for _, j in cells]
        return min(is_), min(js_), max(is_), max(js_)

    def is_border_rect(cells):
        mi, mj, ma, mb = bbox(cells)
        S = set(cells)
        for i in range(mi, ma + 1):
        for j in range(mj, mb + 1):
        on_edge = i in (mi, ma) or j in (mj, mb)
        if on_edge and (i, j) not in S:
        return False
        if not on_edge and (i, j) in S:
        return False
        return True

    frame = None
    for color, cells in comps:
        if color == 5 and is_border_rect(cells):
        frame = cells
        break
    if frame is None:
        return [list(row) for row in g]

    mi, mj, ma, mb = bbox(frame)
    imi, imj, ima, imb = mi + 1, mj + 1, ma - 1, mb - 1
    inner = [(i, j) for i in range(imi, ima + 1) for j in range(imj, imb + 1)]
    inner_nonzero = [(i, j) for (i, j) in inner if g[i][j] != 0]
    if not inner_nonzero:
        return [list(row) for row in g]

    base_i = min(i for i, _ in inner_nonzero)
    base_j = min(j for _, j in inner_nonzero)
    pattern = {(i - base_i, j - base_j) for (i, j) in inner_nonzero}
    pattern_color = Counter(g[i][j] for (i, j) in inner_nonzero).most_common(1)[0][0]

    out = [row[:] for row in g]
    for color, cells in comps:
        mi, mj, ma, mb = bbox(cells)
        norm = {(i - mi, j - mj) for (i, j) in cells}
        if norm == pattern:
        for i, j in cells:
        out[i][j] = pattern_color
    return out
