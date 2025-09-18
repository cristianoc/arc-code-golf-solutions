# ARC Task 185

def p(g):
    # Compact, non‑DSL solution for 7837ac64.
    # Interpret the grid as tiles separated by uniform separator rows/cols.
    # For each tile, output its majority value (excluding the separator color).
    from collections import Counter

    H, W = len(g), len(g[0])

    # Detect separator color from fully - uniform rows/cols
    row_colors = [r[0] if all(v == r[0] for v in r) else None for r in g]
    col_colors = []
    for j in range(W):
        col = [g[i][j] for i in range(H)]
        col_colors.append(col[0] if all(v == col[0] for v in col) else None)
    from collections import Counter as C
    counts = C(c for c in row_colors + col_colors if c is not None)
    sep = (counts.most_common(1)[0][0] if counts else C(v for r in g for v in r).most_common(1)[0][0])

    # Separator indices (tolerant: allow a few non - sep intrusions)
    rc = [sum(1 for v in r if v == sep) for r in g]
    cc = [sum(1 for i in range(H) if g[i][j] == sep) for j in range(W)]
    rmax = max(rc) if rc else 0
    cmax = max(cc) if cc else 0
    tol = 4
    sep_rows = [i for i, c in enumerate(rc) if c >= rmax - tol]
    sep_cols = [j for j, c in enumerate(cc) if c >= cmax - tol]

    def segments(seps, N):
        bounds = [-1] + seps + [N]
        return [(bounds[k] + 1, bounds[k + 1]) for k in range(len(bounds) - 1) if bounds[k + 1] - bounds[k] > 1]

    row_segs = segments(sep_rows, H)
    col_segs = segments(sep_cols, W)
    if not row_segs or not col_segs:
        return [list(row) for row in g]

    # Focus on the region that actually contains markers (non 0/sep).
    pts = [(i, j) for i in range(H) for j in range(W) if g[i][j] not in (0, sep)]
    if pts and len(sep_rows) >= 4 and len(sep_cols) >= 4:
        # Choose 4 consecutive separator rows/cols that capture the most markers
        def best_window(seps, axis = 0):
        best = None
        for a in range(len(seps) - 3):
        lo, hi = seps[a], seps[a + 3]
        if axis == 0:
        cnt = sum(1 for i, _ in pts if lo <= i <= hi)
        else:
        cnt = sum(1 for _, j in pts if lo <= j <= hi)
        if best is None or cnt > best[0]:
        best = (cnt, a)
        a = best[1] if best else 0
        return seps[a : a + 4]
        R = best_window(sep_rows, 0)
        Cc = best_window(sep_cols, 1)
        # Replace segs by the cells between chosen separators
        row_segs = [(R[k], R[k + 1]) for k in range(3)]
        col_segs = [(Cc[k], Cc[k + 1]) for k in range(3)]

    out = []
    for rs, re in row_segs:
        row_vals = []
        for cs, ce in col_segs:
        # Decide by the four corner intersections; require unanimous non - zero, non - sep color.
        corners = [g[rs][cs], g[rs][ce], g[re][cs], g[re][ce]]
        nz = [v for v in corners if v not in (0, sep)]
        row_vals.append(nz[0] if len(nz) == 4 and len(set(nz)) == 1 else 0)
        out.append(row_vals)
    return out
