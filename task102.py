def solve_44d8ac46(I):
    # Ensure tuple-of-tuples
    G = tuple(tuple(r) for r in I)
    h, w = len(G), len(G[0])

    # Background = most frequent color
    from collections import Counter, deque
    cnt = Counter(v for r in G for v in r)
    bg = max(cnt, key=cnt.get)

    # 4-connected components of same color (excluding background)
    visited = [[False] * w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if visited[i][j] or G[i][j] == bg:
                continue
            color = G[i][j]
            q = deque([(i, j)])
            visited[i][j] = True
            comp = {(i, j)}
            while q:
                x, y = q.popleft()
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and G[nx][ny] == color:
                        visited[nx][ny] = True
                        q.append((nx, ny))
                        comp.add((nx, ny))
            comps.append(comp)

    to_fill = set()
    for idx in comps:
        if not idx:
            continue
        si = min(i for i, _ in idx)
        sj = min(j for _, j in idx)
        ei = max(i for i, _ in idx)
        ej = max(j for _, j in idx)
        # Cells inside the bounding box that are not part of the object
        holes = {(i, j) for i in range(si, ei + 1) for j in range(sj, ej + 1) if (i, j) not in idx}
        if not holes:
            continue
        # Check that holes form a solid, perfect square (fills its own bbox)
        hi = min(i for i, _ in holes)
        hj = min(j for _, j in holes)
        he = max(i for i, _ in holes)
        hk = max(j for _, j in holes)
        hh = he - hi + 1
        hw = hk - hj + 1
        if hh == hw and len(holes) == hh * hw:
            to_fill |= holes

    if not to_fill:
        return G

    O = [list(r) for r in G]
    for i, j in to_fill:
        if 0 <= i < h and 0 <= j < w:
            O[i][j] = 2
    return tuple(tuple(r) for r in O)

def p(g):
    R = solve_44d8ac46(g)
    return [list(r) for r in R]

