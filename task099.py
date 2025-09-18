def p(g):
    from collections import deque, Counter
    h, w = len(g), len(g[0])
    bg = Counter(v for r in g for v in r).most_common(1)[0][0]
    out = [row[:] for row in g]
    seen = [[0] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if g[i][j] == 1 and not seen[i][j]:
                q = deque([(i, j)])
                seen[i][j] = 1
                comp = []
                while q:
                    x, y = q.popleft(); comp.append((x, y))
                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        u, v = x + dx, y + dy
                        if 0 <= u < h and 0 <= v < w and not seen[u][v] and g[u][v] == 1:
                            seen[u][v] = 1; q.append((u, v))
                si = min(x for x, _ in comp); ei = max(x for x, _ in comp)
                sj = min(y for _, y in comp); ej = max(y for _, y in comp)
                in_comp = set(comp)
                colors = [g[x][y] for x in range(si, ei + 1) for y in range(sj, ej + 1) if (x, y) not in in_comp]
                if not colors:
                    continue
                cnt = Counter(colors); m = min(cnt.values())
                val = min(c for c, k in cnt.items() if k == m)
                for x in range(si, ei + 1):
                    xx = x - 1
                    if 0 <= xx < h:
                        for y in range(sj, ej + 1):
                            if out[xx][y] == bg:
                                out[xx][y] = val
    return out

