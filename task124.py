# ARC Task 124

def p(g):
    # Compact non - DSL solution for 53b68214 (task124)
    # Fill an output square of size equal to input width by extending the
    # object's vertical periodic pattern; if no smaller period, extend once
    # following the object's last - row trend.
    G = [row[:] for row in g]
    H, W = len(G), len(G[0])

    # Background = most frequent color
    from collections import Counter
    cnt = Counter(v for r in G for v in r)
    bg = max(cnt, key = lambda c: cnt[c])

    # Collect object cells (non - background) with their colors
    obj = [(i, j, G[i][j]) for i in range(H) for j in range(W) if G[i][j] != bg]
    if not obj:
        return [[0] * W for _ in range(W)]

    # Bounding box
    min_i = min(i for i, _, _ in obj)
    max_i = max(i for i, _, _ in obj)
    min_j = min(j for _, j, _ in obj)
    max_j = max(j for _, j, _ in obj)
    h_obj = max_i - min_i + 1
    w_obj = max_j - min_j + 1

    # Normalize indices to start at row 0 for period detection
    idx = {(i - min_i, j): c for i, j, c in obj}

    # Vertical period (smallest p<h_obj where shift up by p is subset)
    p = h_obj
    for k in range(1, h_obj):
        ok = True
        for (i, j), _c in idx.items():
        if i - k >= 0 and (i - k, j) not in idx:
        ok = False
        break
        if ok:
        p = k
        break

    # Prepare output square (zeros/black background)
    O = [[0 for _ in range(W)] for _ in range(W)]

    # Helper to paint a copy shifted by (di, dj)
    def paint_shift(di, dj):
        for i, j, c in obj:
        ii, jj = i + di, j + dj
        if 0 <= ii < W and 0 <= jj < W:
        O[ii][jj] = c

    # Always paint the original object once
    paint_shift(0, 0)

    if p != h_obj:
        # Tile downward by multiples of the vertical period
        for k in range(1, 9):
        paint_shift(k * p, 0)
    else:
        # Extend row - by - row following the last - row repetition trend
        # Gather pixels of each row within object
        rows = {}
        for i, j, c in obj:
        rows.setdefault(i, []).append((j, c))

        # Determine two - row shift using rows of same parity if available
        if (max_i - 2) in rows:
        j_now = min(j for j, _ in rows[max_i])
        j_prev2 = min(j for j, _ in rows[max_i - 2])
        d2 = j_now - j_prev2
        else:
        # Fallback to immediate delta
        if (max_i - 1) in rows and rows[max_i - 1]:
        d2 = min(j for j, _ in rows[max_i]) - min(j for j, _ in rows[max_i - 1])
        else:
        d2 = 0

        # Generate subsequent rows by repeating pattern every 2 rows with shift d2
        for r in range(max_i + 1, W):
        src = r - 2
        base = rows.get(src, rows.get(r - 1, []))
        nxt = []
        for j, c in base:
        jj = j + d2
        if 0 <= jj < W:
        O[r][jj] = c
        nxt.append((jj, c))
        rows[r] = nxt

    return O
