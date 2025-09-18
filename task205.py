# ARC Task 205

def p(g):
    # Guard empty input
    if not g or not g[0]:
        return []

    # Largest 4 - connected monochrome component (by cell count)
    h, w = len(g), len(g[0])
    visited = set()
    best = []
    for i in range(h):
        for j in range(w):
        if (i, j) in visited:
        continue
        color = g[i][j]
        stack = [(i, j)]
        comp = []
        visited.add((i, j))
        while stack:
        ci, cj = stack.pop()
        comp.append((ci, cj))
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        ni, nj = ci + di, cj + dj
        if 0 <= ni < h and 0 <= nj < w and (ni, nj) not in visited and g[ni][nj] == color:
        visited.add((ni, nj))
        stack.append((ni, nj))
        if len(comp) > len(best):
        best = comp

    # Bounding box subgrid around the chosen object
    i0 = min(i for i, _ in best)
    i1 = max(i for i, _ in best)
    j0 = min(j for _, j in best)
    j1 = max(j for _, j in best)
    sub = [row[j0 : j1 + 1] for row in g[i0 : i1 + 1]]
    if not sub:
        return []
    # Start from the raw bounding box; we will clean borders by majority background
    filtered = [row[:] for row in sub]

    # Trim noisy borders: drop outer rows/cols that are not majority background
    vals = [v for r in filtered for v in r]
    bg = max(set(vals), key = vals.count)
    rows = [row[:] for row in filtered]
    H, W = len(rows), len(rows[0])
    # Remove top/bottom rows whose bg fraction <= 0.5
    while rows and sum(1 for v in rows[0] if v == bg) * 2 <= W:
        rows.pop(0)
        H -= 1
    while rows and sum(1 for v in rows[-1] if v == bg) * 2 <= W:
        rows.pop()
        H -= 1
    if not rows:
        return []
    # Remove left/right columns whose bg fraction <= 0.5
    cols = list(zip(*rows))
    while cols and sum(1 for v in cols[0] if v == bg) * 2 <= len(rows):
        cols.pop(0)
    while cols and sum(1 for v in cols[-1] if v == bg) * 2 <= len(rows):
        cols.pop()
    if not cols:
        return []
    filtered = [list(r) for r in zip(*cols)]

    # Background is the most frequent value; rare color defines lines
    vals = [v for r in filtered for v in r]
    bg = max(set(vals), key = vals.count)
    rare = min(set(vals), key = vals.count)
    H, W = len(filtered), len(filtered[0])
    out = [[bg] * W for _ in range(H)]
    pos = [(i, j) for i, r in enumerate(filtered) for j, v in enumerate(r) if v == rare]
    if not pos:
        return out
    rows = {i for i, _ in pos}
    cols = {j for _, j in pos}

    # Avoid overfitting: do not collapse to a single row/col on specific sizes.
    # Instead, draw all lines implied by the positions of the rare color.

    for i in rows:
        out[i] = [rare] * W
    for j in cols:
        for i in range(H):
        out[i][j] = rare
    return out
