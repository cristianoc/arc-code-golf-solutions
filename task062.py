def solve_2bcee788(I):
    H, W = len(I), len(I[0])
    # Most common color (background)
    flat = [v for r in I for v in r]
    bg = max(set(flat), key=flat.count)

    # Find 4-connected, univalued components excluding background (on original I)
    seen = [[False] * W for _ in range(H)]
    comps = []  # list of lists of (i,j)
    for i in range(H):
        for j in range(W):
            if I[i][j] == bg or seen[i][j]:
                continue
            c = I[i][j]
            q = [(i, j)]
            seen[i][j] = True
            cells = []
            while q:
                x, y = q.pop()
                if I[x][y] != c:
                    continue
                cells.append((x, y))
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < H and 0 <= ny < W and not seen[nx][ny] and I[nx][ny] == c:
                        seen[nx][ny] = True
                        q.append((nx, ny))
            if cells:
                comps.append(cells)

    # Largest and smallest components by size
    big = max(comps, key=len)
    small = min(comps, key=len)

    # Bounding boxes
    def bbox(cells):
        is_ = [i for i, _ in cells]
        js_ = [j for _, j in cells]
        mi, ma = min(is_), max(is_)
        mj, mb = min(js_), max(js_)
        return mi, mj, ma, mb

    bi0, bj0, bi1, bj1 = bbox(big)
    si0, sj0, si1, sj1 = bbox(small)

    # Centers using bbox (match DSL center)
    ci_big = bi0 + (bi1 - bi0 + 1) // 2
    cj_big = bj0 + (bj1 - bj0 + 1) // 2
    ci_sml = si0 + (si1 - si0 + 1) // 2
    cj_sml = sj0 + (sj1 - sj0 + 1) // 2

    # Direction vector from big -> small
    if ci_big == ci_sml:
        vec = (0, 1 if cj_big < cj_sml else -1)
    elif cj_big == cj_sml:
        vec = (1 if ci_big < ci_sml else -1, 0)
    elif ci_big < ci_sml:
        vec = (1, 1 if cj_big < cj_sml else -1)
    else:
        vec = (-1, 1 if cj_big < cj_sml else -1)

    # Build grid with background replaced by 3
    R = [list(r) for r in I]
    for i in range(H):
        for j in range(W):
            if R[i][j] == bg:
                R[i][j] = 3

    # Subgrid for big's bbox from R
    sub = [row[bj0:bj1 + 1] for row in R[bi0:bi1 + 1]]

    # Check if smallest is a horizontal line as in DSL: height==1 and width==len(cells)
    h_small = si1 - si0 + 1
    w_small = sj1 - sj0 + 1
    # Choose mirror mode based on overlap/relative positions
    overlap_cols = not (bj1 < sj0 or sj1 < bj0)
    overlap_rows = not (bi1 < si0 or si1 < bi0)
    if overlap_cols and not overlap_rows:
        mirror_horiz = False  # stacked vertically -> mirror vertically
    elif overlap_rows and not overlap_cols:
        mirror_horiz = True   # side-by-side -> mirror horizontally
    else:
        mirror_horiz = abs(ci_big - ci_sml) <= abs(cj_big - cj_sml)

    # Mirror direction: if smallest is a horizontal line, mirror horizontally
    # (left-right) to reflect across the small segment; otherwise mirror vertically.
    sub = [r[::-1] for r in sub] if mirror_horiz else sub[::-1]

    # Base placement: place the mirrored big symmetrically across the small's center
    h_big = bi1 - bi0 + 1
    w_big = bj1 - bj0 + 1
    if mirror_horiz:
        # Mirror across a vertical axis located midway between the two objects
        # Determine which side the small lies and compute edge-based midpoint
        if cj_sml >= cj_big:
            axis = (bj1 + sj0) / 2.0  # between big right edge and small left edge
        else:
            axis = (sj1 + bj0) / 2.0  # between small right edge and big left edge
        # After left-right flip, align via edge formula
        base_i = bi0
        base_j = int(round(2 * axis - bj0 - (w_big - 1)))
    else:
        # Mirror across a horizontal axis located midway between the two objects
        if ci_sml >= ci_big:
            axis = (bi1 + si0) / 2.0  # between big bottom edge and small top edge
        else:
            axis = (si1 + bi0) / 2.0  # between small bottom edge and big top edge
        # After up-down flip, align via edge formula
        base_i = int(round(2 * axis - bi0 - (h_big - 1)))
        base_j = bj0

    # Paint non-3 pixels of mirrored sub onto R with bounds check
    for ii, row in enumerate(sub):
        for jj, v in enumerate(row):
            if v == 3:
                continue
            ti, tj = base_i + ii, base_j + jj
            if 0 <= ti < H and 0 <= tj < W:
                R[ti][tj] = v

    return tuple(tuple(r) for r in R)


def p(g):
    G = tuple(tuple(r) for r in g)
    R = solve_2bcee788(G)
    return [list(r) for r in R]
