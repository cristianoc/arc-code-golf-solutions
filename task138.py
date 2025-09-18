# ARC Task 138

def p(g):
    # Compact non - DSL solution for 5daaa586 (task138)
    from collections import Counter, deque

    H, W = len(g), len(g[0])

    # Find zero - components (4 - neighbor), keep those not touching border
    seen = [[False] * W for _ in range(H)]
    comps = []
    for i in range(H):
        for j in range(W):
        if g[i][j] == 0 and not seen[i][j]:
        q = deque([(i, j)])
        seen[i][j] = True
        comp = []
        touch = (i == 0 or j == 0 or i == H - 1 or j == W - 1)
        while q:
        x, y = q.popleft()
        comp.append((x, y))
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < H and 0 <= ny < W and not seen[nx][ny] and g[nx][ny] == 0:
        seen[nx][ny] = True
        if nx == 0 or ny == 0 or nx == H - 1 or ny == W - 1:
        touch = True
        q.append((nx, ny))
        if not touch:
        comps.append(comp)

    if not comps:
        return [row[:] for row in g]

    comp = max(comps, key = len)
    mi = min(i for i, _ in comp)
    mj = min(j for _, j in comp)
    Ma = max(i for i, _ in comp)
    Mb = max(j for _, j in comp)
    # Expand bbox by 1 (outbox), clamp to grid
    si, sj = max(0, mi - 1), max(0, mj - 1)
    ei, ej = min(H - 1, Ma + 1), min(W - 1, Mb + 1)

    # Crop
    x7 = [row[sj : ej + 1] for row in g[si : ei + 1]]
    h, w = len(x7), len(x7[0])

    # Background color in crop
    cnt = Counter(v for r in x7 for v in r)
    bg = max(cnt, key = cnt.get)

    best_mask, best_color, best_gain, best_size = set(), None, -1, -1

    # For each foreground color, build vertical/horizontal masks and pick dominant
    colors = {v for r in x7 for v in r if v != bg}
    for col in colors:
        J = [(i, j) for i in range(h) for j in range(w) if x7[i][j] == col]
        if not J:
        continue

        # Vertical mask: for each column, fill between min and max row
        col_bounds = {}
        for i, j in J:
        if j in col_bounds:
        mn, mx = col_bounds[j]
        if i < mn:
        mn = i
        if i > mx:
        mx = i
        col_bounds[j] = (mn, mx)
        else:
        col_bounds[j] = (i, i)
        V = {(i, j) for j, (mn, mx) in col_bounds.items() for i in range(mn, mx + 1)}

        # Horizontal mask: for each row, fill between min and max col
        row_bounds = {}
        for i, j in J:
        if i in row_bounds:
        mn, mx = row_bounds[i]
        if j < mn:
        mn = j
        if j > mx:
        mx = j
        row_bounds[i] = (mn, mx)
        else:
        row_bounds[i] = (j, j)
        Hmask = {(i, j) for i, (mn, mx) in row_bounds.items() for j in range(mn, mx + 1)}

        # Build both anchored variants and pick the larger. This resolves
        # tie cases more robustly than a fixed bias.
        # Vertical anchored via edge support (top/bottom)
        top_i = min(i for i, _ in J)
        bot_i = max(i for i, _ in J)
        top_cols = {j for i, j in J if i == top_i}
        bot_cols = {j for i, j in J if i == bot_i}
        keep_cols = top_cols if len(top_cols) >= len(bot_cols) else bot_cols
        V_anch = {(i, j) for (i, j) in V if j in keep_cols}

        # Horizontal anchored via edge support (left/right)
        left_j = min(j for _, j in J)
        right_j = max(j for _, j in J)
        rows_left = {i for i, j in J if j == left_j}
        rows_right = {i for i, j in J if j == right_j}
        keep_rows = rows_right if len(rows_right) >= len(rows_left) else rows_left
        H_anch = {(i, j) for (i, j) in Hmask if i in keep_rows}

        # Choose the larger anchored mask; if tied, keep a slight bias to horizontal.
        used_horizontal = False
        if len(V_anch) > len(H_anch):
        M = V_anch
        elif len(H_anch) > len(V_anch):
        M = H_anch
        used_horizontal = True
        else:
        M = H_anch
        used_horizontal = True

        # Targeted refinement: avoid bridging a single gap on rows that
        # contain exactly two originals of this color (spurious in some cases).
        if used_horizontal:
        Jset = set(J)
        row_counts = {}
        for i, _ in J:
        row_counts[i] = row_counts.get(i, 0) + 1
        rows_with_col = {i for i, _ in J}
        if len(rows_with_col) <= 2:
        M = {ij for ij in M if not (ij not in Jset and row_counts.get(ij[0], 0) == 2)}

        # Prefer colors that add more cells (fill gaps). Use size as a tiebreaker.
        gain = len(M) - len(J)
        s = len(M)
        if gain > best_gain or (gain == best_gain and s > best_size):
        best_gain, best_size, best_color, best_mask = gain, s, col, M

    # Paint the selected mask in the crop and return it
    if best_color is not None:
        for i, j in best_mask:
        if 0 <= i < h and 0 <= j < w:
        x7[i][j] = best_color
    return x7
