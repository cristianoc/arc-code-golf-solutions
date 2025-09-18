def p(g):
    # Compact, non-DSL implementation of d687bc17
    I = tuple(tuple(r) for r in g)
    h, w = len(I), len(I[0])

    def most_color(G):
        from collections import Counter
        c = Counter(v for row in G for v in row)
        return max(c.items(), key=lambda kv: kv[1])[0]

    bg = most_color(I)

    # Majority non-zero color on each border side
    def majority_color(vals):
        from collections import Counter
        cnt = Counter(v for v in vals if v != bg)
        if not cnt:
            return bg
        return max(cnt.items(), key=lambda kv: kv[1])[0]

    top_c = majority_color(I[0])
    bot_c = majority_color(I[-1])
    left_c = majority_color([I[i][0] for i in range(h)])
    right_c = majority_color([I[i][-1] for i in range(h)])

    # Find interior objects (4-connected components not touching border), excluding background
    seen = [[False] * w for _ in range(h)]
    interior = []

    def n4(i, j):
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ni, nj = i + di, j + dj
            if 0 <= ni < h and 0 <= nj < w:
                yield ni, nj

    for i in range(h):
        for j in range(w):
            if seen[i][j]:
                continue
            seen[i][j] = True
            v = I[i][j]
            if v == bg:
                continue
            stack = [(i, j)]
            cells = []
            touches_border = False
            while stack:
                ci, cj = stack.pop()
                cells.append((ci, cj))
                if ci == 0 or ci == h - 1 or cj == 0 or cj == w - 1:
                    touches_border = True
                for ni, nj in n4(ci, cj):
                    if not seen[ni][nj] and I[ni][nj] == v:
                        seen[ni][nj] = True
                        stack.append((ni, nj))
            if not touches_border:
                interior.append((v, cells))

    G = [list(row) for row in I]

    # For each pixel of each interior object, extend matching border one step inward
    for v, cells in interior:
        for (i, j) in cells:
            # top
            if v == top_c and h >= 2:
                ti, tj = 1, max(1, min(w - 2, j))
                G[ti][tj] = top_c
            # bottom
            if v == bot_c and h >= 2:
                bi, bj = h - 2, max(1, min(w - 2, j))
                G[bi][bj] = bot_c
            # left
            if v == left_c and w >= 2:
                li, lj = max(1, min(h - 2, i)), 1
                G[li][lj] = left_c
            # right
            if v == right_c and w >= 2:
                ri, rj = max(1, min(h - 2, i)), w - 2
                G[ri][rj] = right_c

    # Remove interior objects (set to background)
    for _, cells in interior:
        for i, j in cells:
            G[i][j] = bg

    return [list(row) for row in G]

