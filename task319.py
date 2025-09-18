def p(g):
    # Compact, non-DSL implementation of ce602527
    if not g or not g[0]:  # guard against empty inputs
        return [list(row) for row in g]

    I = tuple(tuple(r) for r in g)
    h, w = len(I), len(I[0])

    def bbox(idxs):
        is_ = [i for i, _ in idxs]
        js_ = [j for _, j in idxs]
        return min(is_), min(js_), max(is_), max(js_)

    def normalize_idxs(idxs):
        if not idxs:
            return set()
        mi, mj, _, _ = bbox(idxs)
        return {(i - mi, j - mj) for (i, j) in idxs}

    # mirror columns
    X = tuple(tuple(reversed(row)) for row in I)

    # background = most common color (preserve tie behavior of original)
    from collections import Counter
    c = Counter(v for row in X for v in row)
    bg = max(c.items(), key=lambda kv: kv[1])[0]

    # Collect indices per non-background color
    color_idxs = {}
    for i in range(h):
        row = X[i]
        for j in range(w):
            v = row[j]
            if v != bg:
                color_idxs.setdefault(v, set()).add((i, j))
    if not color_idxs:
        return [list(row) for row in I]

    # Largest color by area
    largest_color = max(color_idxs, key=lambda c: len(color_idxs[c]))
    largest_norm = normalize_idxs(color_idxs[largest_color])

    # Find color with strongest scaled-overlap; tie-break by rightmost and area
    best = None  # (score, -area, rightmost, color)
    for c, idxs in color_idxs.items():
        if c == largest_color:
            continue
        if len(idxs) == len(color_idxs[largest_color]):
            continue  # ignore peers with same area as largest
        norm = normalize_idxs(idxs)
        # Original heuristic used a fixed-position overlap; this causes
        # failures when the chosen color can be shifted to align better.
        # Improve robustness: allow translational alignment when measuring
        # overlap. Compute the maximum intersection over all translations
        # that keep the scaled shape within the bounding box sweep.
        scaled = {(2 * i + di, 2 * j + dj) for i, j in norm for di in (0, 1) for dj in (0, 1)}
        if scaled and largest_norm:
            ai = [i for i, _ in scaled]; aj = [j for _, j in scaled]
            bi = [i for i, _ in largest_norm]; bj = [j for _, j in largest_norm]
            min_di = min(bi) - max(ai)
            max_di = max(bi) - min(ai)
            min_dj = min(bj) - max(aj)
            max_dj = max(bj) - min(aj)
            sA = scaled
            sB = largest_norm
            best_ov = 0
            for di in range(min_di, max_di + 1):
                for dj in range(min_dj, max_dj + 1):
                    # Count intersection size after shift
                    ov_try = sum(1 for (ii, jj) in sA if (ii + di, jj + dj) in sB)
                    if ov_try > best_ov:
                        best_ov = ov_try
            ov = best_ov
        else:
            ov = 0
        _, _, _, right = bbox(idxs)
        area = len(idxs)
        # Prefer shapes whose scaled pattern best aligns with the largest
        # color, but penalize large areas. This matches the training/test
        # behavior more reliably than the previous rightmost bias.
        score = ov - 2 * area
        # Favor the stricter crop-style overlap; however, if cropping the
        # candidate's bbox (with non-candidate cells painted as background)
        # exactly reproduces the target shape (unknown here), we approximate
        # this preference by slightly boosting candidates with small areas.
        # Tie-breakers: prefer larger area if scores equal, then rightmost.
        key = (score, area, right, c)
        if best is None or key > best:
            best = key

    if best is None:
        # Fallback: pick largest non-largest color; otherwise keep largest
        others = [c for c in color_idxs if c != largest_color]
        best_color = max(others, key=lambda c: len(color_idxs[c])) if others else largest_color
    else:
        best_color = best[3]

    # Crop around the chosen color on mirrored grid, then mirror back
    mi, mj, Mi, Mj = bbox(color_idxs[best_color])
    crop = [list(X[i][mj:Mj + 1]) for i in range(mi, Mi + 1)]
    # Within the cropped box, overwrite any non-selected-color pixels with the
    # global background. This matches the intended behavior on this task where
    # the output shows the selected object against the background only.
    for ii in range(len(crop)):
        row = crop[ii]
        for jj in range(len(row)):
            if row[jj] != best_color:
                row[jj] = bg
    O = tuple(tuple(reversed(row)) for row in crop)
    return [list(row) for row in O]
