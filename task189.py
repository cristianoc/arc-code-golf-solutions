# ARC Task 189

def p(g):
    H, W = len(g), len(g[0])

    # BBox of color 3
    c3 = [(i, j) for i in range(H) for j in range(W) if g[i][j] == 3]
    if not c3:
        return [r[:] for r in g]
    is_ = [i for i, _ in c3]
    js_ = [j for _, j in c3]
    mi, mj, ma, mb = min(is_), min(js_), max(is_), max(js_)
    crop = [row[mj:mb + 1] for row in g[mi:ma + 1]]
    z_crop = [(i, j) for i in range(len(crop)) for j in range(len(crop[0])) if crop[i][j] == 0]

    # Optional zero - mask from the 8 - row/8 - col quadrant containing any 3
    r8 = next((i for i, row in enumerate(g) if all(v == 8 for v in row)), None)
    c8 = next((j for j in range(W) if all(g[i][j] == 8 for i in range(H))), None)
    z_shape = None
    if r8 is not None and c8 is not None:
        def quad_of(i, j):
        return (
        0 if i < r8 and j < c8 else
        1 if i < r8 and j > c8 else
        2 if i > r8 and j < c8 else
        3 if i > r8 and j > c8 else
        None
        )
        q = next((quad_of(i, j) for i, j in c3 if quad_of(i, j) is not None), None)
        if q is not None:
        rs = range(0, r8) if q in (0, 1) else range(r8 + 1, H)
        cs = range(0, c8) if q in (0, 2) else range(c8 + 1, W)
        bi, bj = (min(rs) if rs else 0), (min(cs) if cs else 0)
        z_shape = [(i - bi, j - bj) for i in rs for j in cs if g[i][j] == 0]

    # Replace 3 and 8 with 0, then drop uniform rows/cols
    repl = [[0 if v in (3, 8) else v for v in row] for row in g]
    keep_r = [i for i, r in enumerate(repl) if len(set(r)) != 1]
    tmp = [repl[i] for i in keep_r]
    if not tmp:
        return [r[:] for r in g]
    cols = list(zip(*tmp))
    keep_c = [j for j, c in enumerate(cols) if len(set(c)) != 1]
    comp = [[tmp[i][j] for j in keep_c] for i in range(len(tmp))]

    # Zero columns uniform across the bbox vertical span
    if comp and keep_r and keep_c and (mi in keep_r):
        base = keep_r.index(mi)
        ri0, ri1 = max(0, base), min(len(comp) - 1, base + (ma - mi))
        for j in range(len(comp[0])):
        seg = {comp[i][j] for i in range(ri0, ri1 + 1)}
        if seg and len(seg) == 1:
        for i in range(len(comp)):
        comp[i][j] = 0

    # Upscale by 3
    up = [[v for x in row for v in [x] * 3] for row in comp for _ in range(3)]

    # Apply zero masks
    if up:
        uh, uw = len(up), len(up[0])
        if z_shape is not None:
        for i, j in z_shape:
        if 0 <= i < uh and 0 <= j < uw:
        up[i][j] = 0
        else:
        bi = keep_r.index(mi) if mi in keep_r else 0
        bj = keep_c.index(mj) if mj in keep_c else 0
        for i, j in z_crop:
        ui, uj = bi + i, bj + j
        if 0 <= ui < uh and 0 <= uj < uw:
        up[ui][uj] = 0
    return up
