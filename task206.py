# ARC Task 206

def p(g):
    # Copy the non - green object, normalize it, then place it centered on the
    # green (color 5) object with an extra offset of (-1, -1), preserving colors.
    H, W = len(g), len(g[0])
    from collections import Counter, deque
    # Background as most frequent color
    bg = Counter(v for r in g for v in r).most_common(1)[0][0]

    # 4 - connected components over non - background
    seen = [[False]*W for _ in range(H)]
    comps = []
    for i in range(H):
        for j in range(W):
        if g[i][j] == bg or seen[i][j]:
        continue
        q = deque([(i, j)])
        seen[i][j] = True
        cells = []
        while q:
        x, y = q.popleft()
        cells.append((x, y))
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < H and 0 <= ny < W and not seen[nx][ny] and g[nx][ny] != bg:
        seen[nx][ny] = True
        q.append((nx, ny))
        comps.append(cells)

    green = None
    other = None
    for cells in comps:
        if any(g[i][j] == 5 for i, j in cells):
        green = cells
        else:
        other = cells
    if green is None or other is None:
        return [row[:] for row in g]

    gi0 = min(i for i, _ in green)
    gj0 = min(j for _, j in green)
    gi1 = max(i for i, _ in green)
    gj1 = max(j for _, j in green)
    ci = gi0 + (gi1 - gi0)//2
    cj = gj0 + (gj1 - gj0)//2

    oi0 = min(i for i, _ in other)
    oj0 = min(j for _, j in other)

    out = [row[:] for row in g]
    for i, j in other:
        ni = i - oi0 + ci - 1
        nj = j - oj0 + cj - 1
        if 0 <= ni < H and 0 <= nj < W:
        out[ni][nj] = g[i][j]
    return out
