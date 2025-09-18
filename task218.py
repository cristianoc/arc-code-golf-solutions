# ARC Task 218

def p(g):
    # Crop to bbox of non - zeros, then remove consecutive duplicate rows and columns.
    H, W = len(g), len(g[0])
    top, left, bot, right = H, W, -1, -1
    for i in range(H):
        for j in range(W):
        if g[i][j] != 0:
        if i < top: top = i
        if i > bot: bot = i
        if j < left: left = j
        if j > right: right = j
    if bot < 0:
        return [[]]
    box = [tuple(g[i][left:right + 1]) for i in range(top, bot + 1)]
    # Deduplicate consecutive rows
    rows = []
    prev = None
    for r in box:
        if r != prev:
        rows.append(r)
        prev = r
    # Deduplicate consecutive columns
    cols = list(zip(*rows)) if rows else []
    dedup_cols = []
    prev = None
    for c in cols:
        if c != prev:
        dedup_cols.append(c)
        prev = c
    return [list(r) for r in zip(*dedup_cols)] if dedup_cols else []
