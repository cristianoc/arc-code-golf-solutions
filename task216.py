def p(g):
    # Extract the subgrid of the component whose bounding box maximizes
    # (red-count, -width, -height, -top, -left) where red is color 2.
    H, W = len(g), len(g[0])
    from collections import deque

    seen = [[False]*W for _ in range(H)]
    comps = []
    for i in range(H):
        for j in range(W):
            if g[i][j] == 0 or seen[i][j]:
                continue
            q = deque([(i, j)])
            seen[i][j] = True
            cells = []
            while q:
                x, y = q.popleft()
                cells.append((x, y))
                for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < H and 0 <= ny < W and not seen[nx][ny] and g[nx][ny] != 0:
                        seen[nx][ny] = True
                        q.append((nx, ny))
            comps.append(cells)

    def bbox(c):
        i0 = min(i for i, _ in c); j0 = min(j for _, j in c)
        i1 = max(i for i, _ in c); j1 = max(j for _, j in c)
        return i0, j0, i1, j1
    def redcount(c):
        i0, j0, i1, j1 = bbox(c)
        return sum(1 for i in range(i0, i1+1) for j in range(j0, j1+1) if g[i][j] == 2)
    def score(c):
        i0, j0, i1, j1 = bbox(c)
        h = i1 - i0 + 1; w = j1 - j0 + 1
        return (redcount(c), -w, -h, -i0, -j0)

    best = max(comps, key=score)
    i0, j0, i1, j1 = bbox(best)
    return [row[j0:j1+1] for row in g[i0:i1+1]]

