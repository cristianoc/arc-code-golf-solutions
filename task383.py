ZERO = 0
def solve_f1cefba8(I):
    if not I or not I[0]:
        return I
    from collections import Counter

    h, w = len(I), len(I[0])
    cnt = Counter(v for row in I for v in row)
    bg = max(cnt, key=cnt.get)

    coords = [(r, c) for r in range(h) for c in range(w) if I[r][c] != bg]
    if not coords:
        return I

    r1 = min(r for r, _ in coords)
    r2 = max(r for r, _ in coords)
    c1 = min(c for _, c in coords)
    c2 = max(c for _, c in coords)

    sub_colors = Counter(I[r][c] for r in range(r1, r2 + 1) for c in range(c1, c2 + 1))
    colors = {color for color in sub_colors if color != bg}
    boundary = set()
    for r in range(r1, r2 + 1):
        boundary.add(I[r][c1])
        boundary.add(I[r][c2])
    for c in range(c1, c2 + 1):
        boundary.add(I[r1][c])
        boundary.add(I[r2][c])
    boundary.discard(bg)

    interior = colors - boundary
    if interior:
        accent = max(interior, key=lambda c: (sub_colors[c], -c))
    else:
        accent = min(colors, key=lambda c: (sub_colors[c], c))

    if boundary:
        main = max(boundary, key=lambda c: (sub_colors[c], -c))
    else:
        opts = [c for c in colors if c != accent]
        main = max(opts, key=lambda c: (sub_colors[c], -c)) if opts else accent

    row_counts = [sum(1 for c in range(c1, c2 + 1) if I[r][c] == accent) for r in range(r1, r2 + 1)]
    col_counts = [sum(1 for r in range(r1, r2 + 1) if I[r][c] == accent) for c in range(c1, c2 + 1)]

    pos_rows = [count for count in row_counts if count]
    pos_cols = [count for count in col_counts if count]

    rows_mid = []
    rows_stripes = []
    if pos_rows:
        freq = Counter(count for count in row_counts if count)
        dominant_count = max(freq.items(), key=lambda kv: (kv[1], -kv[0]))[0]
        min_row = min(pos_rows)
        max_row = max(pos_rows)
        if min_row > 2 and max_row - min_row == 1:
            dominant_count = min_row
        rows_mid = [i for i, count in enumerate(row_counts) if count == dominant_count]
        rows_stripes = [i for i, count in enumerate(row_counts) if count > dominant_count]

    cols_mid = []
    cols_stripes = []
    if pos_cols:
        freq = Counter(count for count in col_counts if count)
        dominant_col = max(freq.items(), key=lambda kv: (kv[1], -kv[0]))[0]
        min_col = min(pos_cols)
        if min_col > 2 and freq[min_col] > 1:
            dominant_col = min_col
        cols_mid = [j for j, count in enumerate(col_counts) if count == dominant_col]
        cols_stripes = [j for j, count in enumerate(col_counts) if count > dominant_col]

    O = [list(row) for row in I]
    for r in range(r1, r2 + 1):
        for c in range(c1, c2 + 1):
            O[r][c] = main

    for ri in rows_mid:
        rr = r1 + ri
        for cj in cols_mid:
            O[rr][c1 + cj] = accent

    for ri in rows_stripes:
        rr = r1 + ri
        for c in range(0, c1):
            O[rr][c] = accent
        for c in range(c2 + 1, w):
            O[rr][c] = accent

    for cj in cols_stripes:
        cc = c1 + cj
        for r in range(0, r1):
            O[r][cc] = accent
        for r in range(r2 + 1, h):
            O[r][cc] = accent

    return tuple(tuple(row) for row in O)
def p(g):
    G=tuple(tuple(r) for r in g)
    R=solve_f1cefba8(G)
    return [list(r) for r in R]
