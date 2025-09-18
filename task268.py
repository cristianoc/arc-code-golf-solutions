ZERO = 0
FOUR = 4


def mostcolor(grid):
    values = [v for r in grid for v in r]
    return max(set(values), key=values.count)

def ofcolor(grid, value):
    return {(i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value}


def fill(grid, value, cells):
    if not cells:
        # Return a shallow copy to avoid aliasing
        return [list(row) for row in grid]
    h, w = len(grid), len(grid[0])
    out = [list(row) for row in grid]
    for i, j in cells:
        if 0 <= i < h and 0 <= j < w:
            out[i][j] = value
    return out


def bounds(idxs):
    si = min(i for i, _ in idxs)
    sj = min(j for _, j in idxs)
    ei = max(i for i, _ in idxs)
    ej = max(j for _, j in idxs)
    return si, sj, ei, ej


def position(a_idxs, b_idxs):
    asi, asj, aei, aej = bounds(a_idxs)
    bsi, bsj, bei, bej = bounds(b_idxs)
    aci, acj = (asi + aei) // 2, (asj + aej) // 2
    bci, bcj = (bsi + bei) // 2, (bsj + bej) // 2
    if aci == bci:
        return (0, 1 if acj < bcj else -1)
    if acj == bcj:
        return (1 if aci < bci else -1, 0)
    if aci < bci:
        return (1, 1 if acj < bcj else -1)
    if aci > bci:
        return (-1, 1 if acj < bcj else -1)
    return (0, 0)


def dneighbors(loc):
    i, j = loc
    return {(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)}


def connect(a, b):
    ai, aj = a
    bi, bj = b
    if ai == bi:
        sj, ej = (aj, bj) if aj <= bj else (bj, aj)
        return {(ai, j) for j in range(sj, ej + 1)}
    if aj == bj:
        si, ei = (ai, bi) if ai <= bi else (bi, ai)
        return {(i, aj) for i in range(si, ei + 1)}
    di, dj = bi - ai, bj - aj
    # Diagonals at 45 degrees
    if abs(di) == abs(dj):
        si = 1 if di > 0 else -1
        sj = 1 if dj > 0 else -1
        steps = abs(di)
        return {(ai + k * si, aj + k * sj) for k in range(0, steps + 1)}
    return set()


def solve_aba27056(I):
    # Basic guards and types
    if not I or not I[0]:
        return [list(row) for row in I]

    h, w = len(I), len(I[0])
    bg = mostcolor(I)

    # All indices that are not background
    obj_idx = {(i, j) for i in range(h) for j in range(w) if I[i][j] != bg}
    if not obj_idx:
        return [list(row) for row in I]

    si, sj, ei, ej = bounds(obj_idx)

    # Box edges and interior (rectangle minus object)
    bbox_edges = (
        {(i, sj) for i in range(si, ei + 1)}
        | {(i, ej) for i in range(si, ei + 1)}
        | {(si, j) for j in range(sj, ej + 1)}
        | {(ei, j) for j in range(sj, ej + 1)}
    )
    edge_only = bbox_edges - obj_idx
    rect_all = {(i, j) for i in range(si, ei + 1) for j in range(sj, ej + 1)}
    interior = rect_all - obj_idx

    # Choose extension direction using relative positions and zero-density hints
    dir_a = position(interior, edge_only)
    dir_b = position(edge_only, interior)

    edge_zero_counts = {
        "top": sum(1 for j in range(sj, ej + 1) if I[si][j] == bg),
        "bottom": sum(1 for j in range(sj, ej + 1) if I[ei][j] == bg),
        "left": sum(1 for i in range(si, ei + 1) if I[i][sj] == bg),
        "right": sum(1 for i in range(si, ei + 1) if I[i][ej] == bg),
    }
    edge_dir_map = {"top": (-1, 0), "bottom": (1, 0), "left": (0, -1), "right": (0, 1)}
    dominant_edge_dir = None
    edge_candidates = [
        (count, edge_dir_map[name]) for name, count in edge_zero_counts.items() if count
    ]
    if edge_candidates:
        edge_candidates.sort(key=lambda item: item[0], reverse=True)
        if len(edge_candidates) == 1 or edge_candidates[0][0] > edge_candidates[1][0]:
            dominant_edge_dir = edge_candidates[0][1]

    left_zeros = sum(1 for i in range(h) for j in range(0, sj) if I[i][j] == ZERO)
    right_zeros = sum(1 for i in range(h) for j in range(ej + 1, w) if I[i][j] == ZERO)
    up_zeros = sum(1 for i in range(0, si) for j in range(w) if I[i][j] == ZERO)
    down_zeros = sum(1 for i in range(ei + 1, h) for j in range(w) if I[i][j] == ZERO)
    prefer_j = 1 if right_zeros > left_zeros else (-1 if left_zeros > right_zeros else 0)
    prefer_i = 1 if down_zeros > up_zeros else (-1 if up_zeros > down_zeros else 0)

    def score_dir(d):
        di, dj = d
        s = 0
        if prefer_j and dj == prefer_j:
            s += 1
        if prefer_i and di == prefer_i:
            s += 1
        return s

    # Start from the geometrically suggested direction; avoid manufacturing diagonals
    # when both geometric estimates agree. If only one axis shows a clear preference,
    # bias toward that axis.
    direction = dominant_edge_dir
    if direction is None:
        if dir_a == dir_b:
            if prefer_j == 0 and prefer_i != 0:
                direction = (prefer_i, 0)
            elif prefer_i == 0 and prefer_j != 0:
                direction = (0, prefer_j)
            else:
                direction = dir_a
        else:
            direction = max((dir_a, dir_b), key=score_dir)
            if score_dir(direction) == 0 and (prefer_i or prefer_j):
                di = prefer_i if prefer_i else 0
                dj = prefer_j if prefer_j else 0
                if di or dj:
                    direction = (di, dj)

    # Rays from the box edges along direction, limited to original zeros
    di, dj = direction
    shifted_edges = set()
    for m in range(0, 9):
        sdi, sdj = di * m, dj * m
        for (i, j) in edge_only:
            shifted_edges.add((i + sdi, j + sdj))

    filled = fill(I, FOUR, interior)
    zeros_in_I = ofcolor(I, ZERO)
    filled = fill(filled, FOUR, shifted_edges & zeros_in_I)

    # Candidate corners/zeros and connection lines
    # Use corners derived from the available edge cells (edge_only),
    # not simply the full bbox corners. This matches original semantics
    # where corners(x4) computes extremes over x4 itself.
    if edge_only:
        esi, esj, eei, eej = bounds(edge_only)
        box_corners = {(esi, esj), (esi, eej), (eei, esj), (eei, eej)}
    else:
        box_corners = {(si, sj), (si, ej), (ei, sj), (ei, ej)}
    zeros_now = ofcolor(filled, ZERO)
    di, dj = direction
    if dj == 0 and di != 0:
        zeros_now = {loc for loc in zeros_now if sj <= loc[1] <= ej}
    elif di == 0 and dj != 0:
        zeros_now = {loc for loc in zeros_now if si <= loc[0] <= ei}

    use_original_neighbors = (prefer_i == 0 and prefer_j == 0)
    neighbor_grid = I if use_original_neighbors else filled

    def two_zero_neighbors(loc):
        cnt = 0
        for ni, nj in dneighbors(loc):
            if 0 <= ni < h and 0 <= nj < w and neighbor_grid[ni][nj] == ZERO:
                cnt += 1
        return cnt == 2

    def adjacent_to(idxs, loc):
        return any((ni, nj) in idxs for (ni, nj) in dneighbors(loc))

    candidates = [
        z
        for z in zeros_now
        if two_zero_neighbors(z) and adjacent_to(obj_idx, z) and adjacent_to(shifted_edges, z)
    ]

    lines = set()
    for a in box_corners:
        for b in candidates:
            d = (b[0] - a[0], b[1] - a[1])
            end = (a[0] + 42 * d[0], a[1] + 42 * d[1])
            lines |= connect(a, end)

    out = fill(filled, FOUR, lines & zeros_in_I)

    if dominant_edge_dir and interior:
        interior_cols = {j for (_, j) in interior}
        interior_rows = {i for (i, _) in interior}
        if dominant_edge_dir == (-1, 0) and si > 0:
            top_cells = {
                (si - 1, j)
                for j in interior_cols
                if 0 <= j < w and I[si - 1][j] == bg
            }
            if top_cells:
                out = fill(out, FOUR, top_cells)
        elif dominant_edge_dir == (1, 0) and ei + 1 < h:
            bottom_cells = {
                (ei + 1, j)
                for j in interior_cols
                if 0 <= j < w and I[ei + 1][j] == bg
            }
            if bottom_cells:
                out = fill(out, FOUR, bottom_cells)
        elif dominant_edge_dir == (0, -1) and sj > 0:
            left_cells = {
                (i, sj - 1)
                for i in interior_rows
                if 0 <= i < h and I[i][sj - 1] == bg
            }
            if left_cells:
                out = fill(out, FOUR, left_cells)
        elif dominant_edge_dir == (0, 1) and ej + 1 < w:
            right_cells = {
                (i, ej + 1)
                for i in interior_rows
                if 0 <= i < h and I[i][ej + 1] == bg
            }
            if right_cells:
                out = fill(out, FOUR, right_cells)

    # Conditional post-fix: extend one row below when warranted and cleanup stray 4s
    if dominant_edge_dir == (1, 0):
        has_other = any(v not in (ZERO, FOUR) for r in I for v in r)
        br = ei + 1
        if has_other or (0 <= br == len(I) - 1):
            did_extend = False
            if 0 <= br < len(I):
                inner_js = range(sj + 1, ej)

                def has_edge_four(j):
                    return any((sj + 1) <= k < ej and filled[ei][k] == FOUR for k in (j - 1, j, j + 1))

                ext_cols = tuple(j for j in inner_js if I[br][j] == ZERO and has_edge_four(j))
                if ext_cols:
                    ext = {(br, j) for j in ext_cols}
                    out = fill(out, FOUR, ext)
                    did_extend = True

            if did_extend:
                w = len(I[0])
                clr = {(ei, j) for j in range(w) if (j < sj or j > ej) and out[ei][j] == FOUR}
                if clr:
                    out = fill(out, ZERO, clr)

    return out


p = solve_aba27056
