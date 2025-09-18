def p(g):
    # Convert to immutable for easier handling
    I = tuple(tuple(r) for r in g)
    h, w = len(I), len(I[0])

    # 4-connected components by color
    seen = [[False]*w for _ in range(h)]
    comps = []  # list of (color, set_of_cells)

    def n4(i, j):
        for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni, nj = i+di, j+dj
            if 0 <= ni < h and 0 <= nj < w:
                yield ni, nj

    for i in range(h):
        for j in range(w):
            if not seen[i][j]:
                col = I[i][j]
                # BFS/DFS
                stack = [(i,j)]
                seen[i][j] = True
                cells = set()
                while stack:
                    ci, cj = stack.pop()
                    cells.add((ci,cj))
                    for ni, nj in n4(ci, cj):
                        if not seen[ni][nj] and I[ni][nj] == col:
                            seen[ni][nj] = True
                            stack.append((ni,nj))
                comps.append((col, cells))

    # Split markers and main objects
    markers = [(c, s) for c, s in comps if len(s) == 1]
    mains = [(c, s) for c, s in comps if len(s) > 1]

    # Take two colors from main objects by total area (size), descending
    if not mains:
        return [list(r) for r in I]
    area = {}
    for c, s in mains:
        area[c] = area.get(c, 0) + len(s)
    main_sorted = sorted(area.items(), key=lambda kv: (-kv[1], kv[0]))
    if not main_sorted:
        return [list(r) for r in I]
    cA = main_sorted[0][0]
    cB = main_sorted[1][0] if len(main_sorted) > 1 else main_sorted[0][0]

    # Cells of color helpers
    SA = {(i,j) for i in range(h) for j in range(w) if I[i][j] == cA}
    SB = {(i,j) for i in range(h) for j in range(w) if I[i][j] == cB}

    # Shoot diagonals from each marker center
    dirs = [(1,1), (-1,-1), (1,-1), (-1,1)]

    def shoot(i, j, di, dj):
        out = []
        ci, cj = i, j
        # include start per description
        while 0 <= ci < h and 0 <= cj < w:
            out.append((ci,cj))
            ci += di
            cj += dj
        return out

    # Prefer markers whose color is not one of the two main colors
    markers_use = [(c, s) for c, s in markers if c not in (cA, cB)]
    if not markers_use:
        markers_use = markers[:]

    R = set()
    for _, s in markers_use:
        (mi, mj) = next(iter(s))
        for di, dj in dirs:
            R.update(shoot(mi, mj, di, dj))

    # Intersections with each main color set
    RA = R & SA
    RB = R & SB

    # Decide mapping using marker placement first, then overlaps/votes as tie-breakers
    if markers_use:
        # unique marker colors in order of frequency
        freq = {}
        for c, _ in markers_use:
            freq[c] = freq.get(c, 0) + 1
        mcolors = sorted(freq.keys(), key=lambda c: (-freq[c], c))
        if len(mcolors) == 1:
            mcolors = mcolors + [mcolors[0]]
        elif len(mcolors) > 2:
            mcolors = mcolors[:2]
        m0c, m1c = mcolors[0], mcolors[1]

        # helper: neighborhood vote (8-neigh) preference for cA vs cB per marker color
        def vote_for(mc):
            a = b = 0
            for c, s in markers_use:
                if c != mc:
                    continue
                (mi, mj) = next(iter(s))
                for di in (-1,0,1):
                    for dj in (-1,0,1):
                        if di == 0 and dj == 0:
                            continue
                        ni, nj = mi+di, mj+dj
                        if 0 <= ni < h and 0 <= nj < w:
                            v = I[ni][nj]
                            if v == cA:
                                a += 1
                            elif v == cB:
                                b += 1
            return a - b  # positive -> closer to A, negative -> closer to B

        # helper: line overlaps from markers of a given color

        # Primary: neighborhood votes (marker sits "on" or nearer to A or B)
        v0 = vote_for(m0c)
        v1 = vote_for(m1c)
        if v0 > 0 and v1 < 0:
            mapA, mapB = m0c, m1c
        elif v0 < 0 and v1 > 0:
            mapA, mapB = m1c, m0c
        elif v0 == 0 and v1 != 0:
            if v1 > 0:
                mapA, mapB = m1c, m0c
            else:
                mapA, mapB = m0c, m1c
        elif v1 == 0 and v0 != 0:
            if v0 > 0:
                mapA, mapB = m0c, m1c
            else:
                mapA, mapB = m1c, m0c
        else:
            # Fallback to overlap-based scoring
            a0, b0 = overlaps_for(m0c)
            a1, b1 = overlaps_for(m1c)
            if a0 > b0 and a1 < b1:
                mapA, mapB = m0c, m1c
            elif a0 < b0 and a1 > b1:
                mapA, mapB = m1c, m0c
            else:
                score_opt1 = a0 + b1
                score_opt2 = a1 + b0
                if score_opt1 > score_opt2:
                    mapA, mapB = m0c, m1c
                elif score_opt2 > score_opt1:
                    mapA, mapB = m1c, m0c
                else:
                    mapA, mapB = (m0c, m1c) if m0c <= m1c else (m1c, m0c)
    else:
        # No markers; nothing to recolor
        return [list(r) for r in I]

    # Apply recoloring on copies
    out = [list(row) for row in I]
    for i, j in RA:
        out[i][j] = mapA
    for i, j in RB:
        out[i][j] = mapB
    return out
