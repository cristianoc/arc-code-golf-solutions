# ARC Task 355

def p(g):
    if not g or not g[0]:
        return [[0]]

    from collections import Counter

    h, w = len(g), len(g[0])
    flat = [x for row in g for x in row]
    # Rare color (least frequent overall)
    Z = min(set(flat), key = flat.count)

    # Find horizontal/vertical cuts that best explain a 2x2 block layout.
    # For each possible cut, score by how many cells are covered by the two
    # most frequent colors on each side, then pick the best.
    def best_hcut():
        best, bestk = -1, 0
        for k in range(h - 1):
        top = [x for r in range(0, k + 1) for x in g[r]]
        bot = [x for r in range(k + 1, h) for x in g[r]]
        ct, cb = Counter(top), Counter(bot)
        score = sum(v for _, v in ct.most_common(2)) + sum(v for _, v in cb.most_common(2))
        if score > best:
        best, bestk = score, k
        return bestk

    def best_vcut():
        best, bestk = -1, 0
        for k in range(w - 1):
        left = [g[r][c] for r in range(h) for c in range(0, k + 1)]
        right = [g[r][c] for r in range(h) for c in range(k + 1, w)]
        cl, cr = Counter(left), Counter(right)
        score = sum(v for _, v in cl.most_common(2)) + sum(v for _, v in cr.most_common(2))
        if score > best:
        best, bestk = score, k
        return bestk

    hc = best_hcut()
    vc = best_vcut()

    # Count rare - color occurrences per quadrant and take that quadrant's base
    # color (mode excluding the rare color).
    def quad_vals(r1, r2, c1, c2):
        return [g[r][c] for r in range(r1, r2) for c in range(c1, c2)]

    quads = (
        quad_vals(0, hc + 1, 0, vc + 1),      # TL
        quad_vals(0, hc + 1, vc + 1, w),      # TR
        quad_vals(hc + 1, h, 0, vc + 1),      # BL
        quad_vals(hc + 1, h, vc + 1, w),      # BR
    )

    best = (-1, -1)  # (Zcount, baseColor)
    for vals in quads:
        cnt = Counter(vals)
        zc = cnt.get(Z, 0)
        base = max(((v, k) for k, v in cnt.items() if k != Z), default = (0, 0))[1]
        # Prefer higher base color on ties to be consistent
        cand = (zc, base)
        if cand > best:
        best = cand

    return [[best[1] if best[0] >= 0 else 0]]
