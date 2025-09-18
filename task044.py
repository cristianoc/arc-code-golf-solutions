def solve_228f6490(I):
    # Compact solution with guards; preserves behavior and I/O.
    if not I or not I[0]:
        return [list(r) for r in I]

    H, W = len(I), len(I[0])

    def n4(i, j):
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ni, nj = i + di, j + dj
            if 0 <= ni < H and 0 <= nj < W:
                yield ni, nj

    # Collect components by color (including zeros)
    seen = [[False] * W for _ in range(H)]
    comps = []  # each: {"color": int, "idx": [(i,j), ...]}
    for i in range(H):
        for j in range(W):
            if seen[i][j]:
                continue
            c = I[i][j]
            stack = [(i, j)]
            seen[i][j] = True
            idx = []
            while stack:
                ci, cj = stack.pop()
                if I[ci][cj] != c:
                    continue
                idx.append((ci, cj))
                for ni, nj in n4(ci, cj):
                    if not seen[ni][nj] and I[ni][nj] == c:
                        seen[ni][nj] = True
                        stack.append((ni, nj))
            if idx:
                comps.append({"color": c, "idx": idx})

    def ulcorner(indices):
        mi = min(i for i, _ in indices)
        mj = min(j for _, j in indices)
        return (mi, mj)

    def border_touch(indices):
        return any(i in (0, H - 1) or j in (0, W - 1) for i, j in indices)

    def normalize(indices):
        ui, uj = ulcorner(indices)
        return tuple(sorted((i - ui, j - uj) for i, j in indices))

    # Shapes available among sources (normalized)
    src_shapes = {}
    for s in comps:
        if s["color"] == 0:
            continue
        key = normalize(s["idx"])
        src_shapes.setdefault(key, []).append(s)

    # Holes = zero components not touching border and matching a source shape
    holes = [h for h in comps if h["color"] == 0 and not border_touch(h["idx"]) and normalize(h["idx"]) in src_shapes]

    # Prefer holes whose boundary touches only the dominant non-zero color (P)
    from collections import Counter
    cnt = Counter(v for r in I for v in r if v != 0)
    P = max(cnt, key=cnt.get) if cnt else None

    def boundary_colors(indices):
        bc=set()
        for i,j in indices:
            for ni,nj in n4(i,j):
                v=I[ni][nj]
                if v!=0:
                    bc.add(v)
        return bc

    if P is not None:
        good=[h for h in holes if all(c==P for c in boundary_colors(h["idx"]))]
        if len(good)>=2:
            holes=good
    holes.sort(key=lambda c: len(c["idx"]), reverse=True)
    if len(holes) < 2:
        return [row[:] for row in I]
    x6, x7 = holes[0], holes[1]

    # Build candidates for each hole: prefer excluding color 5; fallback if none
    def candidates_for(h):
        key = normalize(h["idx"])
        pool = src_shapes.get(key, [])
        cands = [s for s in pool if s["color"] != 5]
        return cands if cands else list(pool)

    c1, c2 = candidates_for(x6), candidates_for(x7)
    # Match previous behavior: if either hole has no candidate, do not move anything.
    if not c1 or not c2:
        return [row[:] for row in I]

    # If both holes expect the same shape, map by spatial order (UL->UL)
    k1, k2 = normalize(x6["idx"]), normalize(x7["idx"])
    s1 = s2 = None
    if k1 == k2:
        # Build a shared candidate pool (prefer excluding color 5; fallback to include it)
        pool = [s for s in src_shapes.get(k1, []) if s["color"] != 5]
        if len(pool) < 2:
            pool = list(src_shapes.get(k1, []))
        if len(pool) < 2:
            return [row[:] for row in I]
        # Sort holes and sources by UL corner; assign in order
        holes_sorted = sorted([(ulcorner(x6["idx"]), 0, x6), (ulcorner(x7["idx"]), 1, x7)])
        pool_sorted = sorted(pool, key=lambda s: ulcorner(s["idx"]))
        a, b = pool_sorted[0], pool_sorted[1]
        # Map according to hole order
        if holes_sorted[0][1] == 0:
            s1, s2 = a, b
        else:
            s1, s2 = b, a
    else:
        # Different shapes: choose per hole with a mild preference
        from collections import Counter

        freq = Counter(v for r in I for v in r)

        def choose(cands, hole):
            if not cands:
                return None
            hu = ulcorner(hole["idx"])
            return min(
                cands,
                key=lambda o: (
                    freq.get(o["color"], 0),
                    abs(ulcorner(o["idx"])[0] - hu[0]) + abs(ulcorner(o["idx"])[1] - hu[1]),
                    o["color"],
                ),
            )

        s1, s2 = choose(c1, x6), choose(c2, x7)

    out = [row[:] for row in I]

    def move_into(src, hole):
        if not src:
            return
        su = ulcorner(src["idx"]) ; hu = ulcorner(hole["idx"]) ; di = hu[0] - su[0] ; dj = hu[1] - su[1]
        for i, j in src["idx"]:
            out[i][j] = 0
        col = src["color"]
        for i, j in src["idx"]:
            ni, nj = i + di, j + dj
            if 0 <= ni < H and 0 <= nj < W:
                out[ni][nj] = col

    move_into(s1, x6)
    move_into(s2, x7)

    return out

def p(g):
    try:
        return solve_228f6490([row[:] for row in g])
    except Exception:
        return [list(r) for r in g]
