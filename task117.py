# ARC Task 117

def solve_4c5c2cf0(I):
    H, W = len(I), len(I[0])

    def most_color(G):
        flat = [v for r in G for v in r]
        return max(set(flat), key = flat.count)

    def rot90(G):
        return tuple(tuple(r) for r in zip(*G[::-1]))

    def hmirror(G):
        return G[::-1]

    def vmirror(G):
        return tuple(tuple(row[::-1]) for row in G)

    def bbox_from_indices(idx):
        is_ = [i for i, _ in idx]
        js_ = [j for _, j in idx]
        return min(is_), min(js_), max(is_), max(js_)

    def center_from_indices(idx):
        u, l, d, r = bbox_from_indices(idx)
        return (u + (d - u) // 2, l + (r - l) // 2)

    def crop(G, u, l, d, r):
        return tuple(tuple(G[i][l:r + 1]) for i in range(u, d + 1))

    def paint(G, obj):
        M = [list(row) for row in G]
        for v, (i, j) in obj:
        if 0 <= i < len(M) and 0 <= j < len(M[0]):
        M[i][j] = v
        return tuple(tuple(r) for r in M)

    def shift_obj(obj, di, dj):
        return {(v, (i + di, j + dj)) for v, (i, j) in obj}

    def components(G, univalued = True, ignore_bg = True):
        # Replicate original behavior:
        # - univalued = True: one object per color (excluding bg), collecting ALL cells of that color
        # - univalued = False: single object of ALL non - bg cells
        bg = most_color(G) if ignore_bg else None
        Hh, Ww = len(G), len(G[0])
        if univalued:
        colors = sorted({G[i][j] for i in range(Hh) for j in range(Ww) if (not ignore_bg or G[i][j] != bg)})
        comps = []
        for c in colors:
        if ignore_bg and c == bg:
        continue
        cells = [(i, j) for i in range(Hh) for j in range(Ww) if G[i][j] == c]
        if cells:
        comps.append({(c, (i, j)) for i, j in cells})
        return comps
        else:
        cells = [(i, j) for i in range(Hh) for j in range(Ww) if (not ignore_bg or G[i][j] != bg)]
        if ignore_bg:
        cells = [(i, j) for (i, j) in cells if G[i][j] != bg]
        if not cells:
        return []
        return [{(G[i][j], (i, j)) for i, j in cells}]

    def subgrid_from_obj(G, obj):
        idx = [(i, j) for _, (i, j) in obj]
        u, l, d, r = bbox_from_indices(idx)
        return crop(G, u, l, d, r), (u, l, d, r)

    def is_rot90_equal(obj, G):
        sg, _ = subgrid_from_obj(G, obj)
        return sg == rot90(sg)

    # Phase 1: find a univalued object in I whose subgrid equals its 90° rotation
    uni = components(I, univalued = True, ignore_bg = True)
    uni_sorted = sorted(uni, key = lambda o: bbox_from_indices([p for _, p in o]))
    x7 = None
    for o in uni_sorted:
        if is_rot90_equal(o, I):
        x7 = o
        break
    if x7 is None:
        return I
    x8 = center_from_indices([p for _, p in x7])

    multi = components(I, univalued = False, ignore_bg = True)
    if not multi:
        return I
    x3 = sorted(multi, key = lambda o: bbox_from_indices([p for _, p in o]))[0]

    # Mirror subgrid of multi - valued object horizontally and extract analogous pieces
    x9, _ = subgrid_from_obj(I, x3)
    x10 = hmirror(x9)

    m_multi = components(x10, univalued = False, ignore_bg = True)
    if not m_multi:
        return I
    x12 = sorted(m_multi, key = lambda o: bbox_from_indices([p for _, p in o]))[0]

    m_uni = components(x10, univalued = True, ignore_bg = True)
    x16 = None
    for o in sorted(m_uni, key = lambda o: bbox_from_indices([p for _, p in o])):
        if is_rot90_equal(o, x10):
        x16 = o
        break
    if x16 is None:
        return I
    x17 = center_from_indices([p for _, p in x16])

    di, dj = (x8[0] - x17[0], x8[1] - x17[1])
    x20 = paint(I, shift_obj(x12, di, dj))

    # Phase 2: vertical mirror and align using color of x7
    x21 = components(x20, univalued = False, ignore_bg = True)
    if not x21:
        return x20
    x22 = sorted(x21, key = lambda o: bbox_from_indices([p for _, p in o]))[0]
    x23, _ = subgrid_from_obj(x20, x22)
    x24 = vmirror(x23)

    x25 = components(x24, univalued = False, ignore_bg = True)
    if not x25:
        return x20
    x26 = sorted(x25, key = lambda o: bbox_from_indices([p for _, p in o]))[0]

    x27 = components(x24, univalued = True, ignore_bg = True)
    if not x27:
        return x20
    target_color = next(iter(x7))[0]
    x30 = None
    for o in sorted(x27, key = lambda o: bbox_from_indices([p for _, p in o])):
        if next(iter(o))[0] == target_color:
        x30 = o
        break
    if x30 is None:
        return x20
    x31 = center_from_indices([p for _, p in x30])
    di2, dj2 = (x8[0] - x31[0], x8[1] - x31[1])
    return paint(x20, shift_obj(x26, di2, dj2))

def p(g):
    G = tuple(tuple(r) for r in g)
    out = solve_4c5c2cf0(G)
    return [list(r) for r in out]
