def p(g):
    h, w = len(g), len(g[0])
    out = [r[:] for r in g]
    seen = [[False]*w for _ in range(h)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]

    for i in range(h):
        for j in range(w):
            if g[i][j] != 0 or seen[i][j]:
                continue
            # BFS on black component
            q = [(i, j)]
            seen[i][j] = True
            cells = [(i, j)]
            min_i = max_i = i
            min_j = max_j = j
            while q:
                ci, cj = q.pop()
                for di, dj in dirs:
                    ni, nj = ci+di, cj+dj
                    if 0 <= ni < h and 0 <= nj < w and not seen[ni][nj] and g[ni][nj] == 0:
                        seen[ni][nj] = True
                        q.append((ni, nj))
                        cells.append((ni, nj))
                        if ni < min_i: min_i = ni
                        if ni > max_i: max_i = ni
                        if nj < min_j: min_j = nj
                        if nj > max_j: max_j = nj
            H = max_i - min_i + 1
            W = max_j - min_j + 1
            color = 4
            if H == W and len(cells) > 1 and len(cells) == H*W:
                color = 3
            for ci, cj in cells:
                out[ci][cj] = color
    return out

