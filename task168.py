def p(g):
    # Compact, non-DSL implementation of 6e19193c (task168)
    G = [row[:] for row in g]
    H, W = len(G), len(G[0])

    from collections import Counter, deque

    def least_color(grid):
        cnt = Counter(v for r in grid for v in r)
        return min(cnt, key=lambda c: cnt[c])

    def most_color(grid):
        cnt = Counter(v for r in grid for v in r)
        return max(cnt, key=lambda c: cnt[c])

    def four_neighbors(i, j):
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ii, jj = i + di, j + dj
            if 0 <= ii < H and 0 <= jj < W:
                yield (ii, jj)

    def objects_univalued_4c_nonbg(grid):
        bg = most_color(grid)
        seen = [[False] * W for _ in range(H)]
        objs = []
        for i in range(H):
            for j in range(W):
                if seen[i][j]:
                    continue
                v = grid[i][j]
                if v == bg:
                    seen[i][j] = True
                    continue
                # BFS univalued region
                col = v
                comp = []
                q = deque([(i, j)])
                seen[i][j] = True
                while q:
                    a, b = q.popleft()
                    if grid[a][b] != col:
                        continue
                    comp.append((a, b))
                    for na, nb in four_neighbors(a, b):
                        if not seen[na][nb]:
                            seen[na][nb] = True
                            q.append((na, nb))
                if comp:
                    # store as list of coordinates for simplicity
                    objs.append((col, comp))
        return objs

    def bbox(points):
        is_ = [i for i, _ in points]
        js_ = [j for _, j in points]
        return (min(is_), min(js_), max(is_), max(js_))

    def delta(points):
        if not points:
            return set()
        si, sj, ei, ej = bbox(points)
        box = {(i, j) for i in range(si, ei + 1) for j in range(sj, ej + 1)}
        return box.difference(set(points))

    def count_in_neigh_color(i, j, color):
        return sum(1 for a, b in four_neighbors(i, j) if G[a][b] == color)

    def shoot(start, direction):
        di, dj = direction
        di = 0 if di == 0 else (1 if di > 0 else -1)
        dj = 0 if dj == 0 else (1 if dj > 0 else -1)
        ai, aj = start
        pts = []
        for k in range(43):
            ii, jj = ai + di * k, aj + dj * k
            if 0 <= ii < H and 0 <= jj < W:
                pts.append((ii, jj))
        return pts

    lc = least_color(G)
    objs = objects_univalued_4c_nonbg(G)

    # Aggregate all shot lines and all deltas
    shot_cells = set()
    delta_cells = set()
    for col, pts in objs:
        d = delta(pts)
        if not d:
            continue
        start = next(iter(d))
        # Pick a point in the object whose 4-neighborhood has exactly two lc
        cand = None
        for i, j in pts:
            if count_in_neigh_color(i, j, lc) == 2:
                cand = (i, j)
                break
        if cand is None:
            # Fallback: just aim towards ulcorner
            ci, cj = min(pts)
            cand = (ci, cj)
        di, dj = start[0] - cand[0], start[1] - cand[1]
        for cell in shoot(start, (di, dj)):
            shot_cells.add(cell)
        delta_cells |= d

    O = [row[:] for row in G]
    for i, j in shot_cells:
        O[i][j] = lc
    for i, j in delta_cells:
        O[i][j] = 0
    return O
