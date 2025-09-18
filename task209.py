# ARC Task 209

def p(g):
    # Non - DSL reimplementation of solve_8a004b2b (preserve exact behavior)
    if not g or not g[0]:  # guard against empty inputs
        return [row[:] for row in g]

    H, W = len(g), len(g[0])

    def objs(G, univalued, diagonal, without_bg):
        from collections import Counter
        bg = Counter(v for r in G for v in r).most_common(1)[0][0] if without_bg else None
        seen = [[False] * W for _ in range(H)]
        res = []
        neigh = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        if diagonal:
        neigh += [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        for i in range(H):
        for j in range(W):
        v = G[i][j]
        if (without_bg and v == bg) or seen[i][j]:
        continue
        comp = []
        stack = [(i, j)]
        seen[i][j] = True
        base = v
        while stack:
        x, y = stack.pop()
        v2 = G[x][y]
        if (univalued and v2 != base) or (without_bg and v2 == bg):
        continue
        comp.append((v2, (x, y)))
        for dx, dy in neigh:
        nx, ny = x + dx, y + dy
        if 0 <= nx < H and 0 <= ny < W and not seen[nx][ny]:
        seen[nx][ny] = True
        stack.append((nx, ny))
        if comp:
        res.append(comp)
        return res

    def toidx(patch):
        return [ij for _, ij in patch] if patch and isinstance(patch[0], tuple) and isinstance(patch[0][1], tuple) else list(patch)

    def leftmost(patch):
        return min(j for _, j in toidx(patch))
    def rightmost(patch):
        return max(j for _, j in toidx(patch))
    def uppermost(patch):
        return min(i for i, _ in toidx(patch))
    def lowermost(patch):
        return max(i for i, _ in toidx(patch))
    def width(patch):
        return rightmost(patch) - leftmost(patch) + 1
    def height(patch):
        return lowermost(patch) - uppermost(patch) + 1
    def ulcorner(patch):
        return (uppermost(patch), leftmost(patch))
    def shift(patch, d):
        di, dj = d
        return [(v, (i + di, j + dj)) for v, (i, j) in patch]
    def normalize(patch):
        return shift(patch, (-uppermost(patch), -leftmost(patch)))
    def merge(cont):
        seen, res = set(), []
        for c in cont:
        for v, (i, j) in c:
        if (i, j) not in seen:
        seen.add((i, j))
        res.append((v, (i, j)))
        return res
    def upscale(patch, f):
        if f <= 1:
        return patch
        res = []
        for v, (i, j) in patch:
        for di in range(f):
        for dj in range(f):
        res.append((v, (i * f + di, j * f + dj)))
        return res
    def paint(G, obj):
        out = [row[:] for row in G]
        for v, (i, j) in obj:
        if 0 <= i < len(out) and 0 <= j < len(out[0]):
        out[i][j] = v
        return out
    def subgrid(patch, G):
        i0, j0 = ulcorner(patch)
        h, w = height(patch), width(patch)
        return [G[i][j0:j0 + w] for i in range(i0, i0 + h)]

    def color_boxes(patch):
        boxes = {}
        for v, (i, j) in patch:
        if v in (0, 4):
        continue
        box = boxes.setdefault(v, [i, i, j, j])
        if i < box[0]:
        box[0] = i
        if i > box[1]:
        box[1] = i
        if j < box[2]:
        box[2] = j
        if j > box[3]:
        box[3] = j
        return boxes

    def ceil_div(a, b):
        return (a + b - 1) // b if b > 0 else 0

    def infer_scale_and_offset(legend_patch, interior_boxes, interior_counts):
        from collections import Counter
        legend_boxes = color_boxes(legend_patch)
        legend_counts = Counter(v for v, _ in legend_patch if v not in (0, 4))
        common = [c for c in legend_boxes if c in interior_boxes]
        if not common:
        return None
        w_ratios, h_ratios = [], []
        ref = []
        count_factors = []
        for c in common:
        li0, li1, lj0, lj1 = legend_boxes[c]
        ii0, ii1, ij0, ij1 = interior_boxes[c]
        lw = lj1 - lj0 + 1
        lh = li1 - li0 + 1
        iw = ij1 - ij0 + 1
        ih = ii1 - ii0 + 1
        if lw <= 0 or lh <= 0 or iw <= 0 or ih <= 0:
        return None
        wr = max(1, ceil_div(iw, lw))
        hr = max(1, ceil_div(ih, lh))
        w_ratios.append(wr)
        h_ratios.append(hr)
        ref.append((li0, lj0, ii0, ij0))
        lcnt = legend_counts.get(c, 0)
        icnt = interior_counts.get(c, 0)
        if lcnt > 0:
        f_color = 1
        while lcnt * f_color * f_color < icnt:
        f_color += 1
        count_factors.append(f_color)
        all_factors = w_ratios + h_ratios + count_factors
        f = max(all_factors) if all_factors else 0
        if f <= 0:
        return None
        offset_is = [ii0 - li0 * f for li0, _, ii0, _ in ref]
        offset_js = [ij0 - lj0 * f for _, lj0, _, ij0 in ref]
        oi = min(offset_is) if offset_is else 0
        oj = min(offset_js) if offset_js else 0
        return f, (oi, oj), ref

    # 1) Find miniature exemplar: objects over whole grid with 4->0, diag, without bg
    G0 = [row[:] for row in g]
    for i in range(H):
        for j in range(W):
        if G0[i][j] == 4:
        G0[i][j] = 0
    candidates = objs(G0, False, True, True)

    # 2) Crop to frame
    frame_idx = [(0, (i, j)) for i in range(H) for j in range(W) if g[i][j] == 4]
    x3 = subgrid(frame_idx, g)

    # 3) Prefer bottom - most among candidates
    lm = max(map(lowermost, candidates)) if candidates else 0
    prelim = [o for o in candidates if lowermost(o) == lm] or candidates

    # 4) Inside crop (with 4->0), union of univalued 4 - neigh objects
    x6 = [[0 if v == 4 else v for v in row] for row in x3]
    ch, cw = (len(x6), len(x6[0])) if x6 and x6[0] else (0, 0)

    def objs_crop(Gc):
        from collections import Counter, deque
        if not Gc or not Gc[0]:
        return []
        cbg = Counter(v for r in Gc for v in r).most_common(1)[0][0]
        seen = [[False] * cw for _ in range(ch)]
        out = []
        for i in range(ch):
        for j in range(cw):
        if seen[i][j] or Gc[i][j] == cbg:
        continue
        base = Gc[i][j]
        q, comp = deque([(i, j)]), []
        seen[i][j] = True
        while q:
        x, y = q.popleft()
        if Gc[x][y] != base or Gc[x][y] == cbg:
        continue
        comp.append((Gc[x][y], (x, y)))
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < ch and 0 <= ny < cw and not seen[nx][ny]:
        if Gc[nx][ny] == base and Gc[nx][ny] != cbg:
        seen[nx][ny] = True
        q.append((nx, ny))
        if comp:
        out.append(comp)
        return out

    x8 = merge(objs_crop(x6))
    idx8 = set(toidx(x8))
    w8, h8 = (width(x8), height(x8)) if x8 else (0, 0)
    i8, j8 = ulcorner(x8) if x8 else (0, 0)
    interior_boxes = color_boxes(x8)
    from collections import Counter as _Counter
    interior_counts = _Counter(v for v, _ in x8)
    interior_map = {(i, j): v for v, (i, j) in x8}

    def clamp_offset(off, max_off):
        if max_off < 0:
        return 0
        if off < 0:
        return 0
        if off > max_off:
        return max_off
        return off

    def offsets_from_ref(ref_data, scale):
        if not ref_data:
        return 0, 0
        offset_is = [ii0 - li0 * scale for li0, _, ii0, _ in ref_data]
        offset_js = [ij0 - lj0 * scale for _, lj0, _, ij0 in ref_data]
        return (min(offset_is) if offset_is else 0, min(offset_js) if offset_js else 0)

    # Evaluate candidates by how well their scaled footprint matches interior union
    best_score, best_patch = None, None
    for x4 in prelim or []:
        if not x4:
        continue
        x5 = normalize(x4)
        inf = infer_scale_and_offset(x5, interior_boxes, interior_counts)
        f_candidates = []
        if inf:
        base_f, base_offset, ref = inf
        f_candidates.append((base_f, base_offset, ref))
        f_candidates.append((base_f + 1, offsets_from_ref(ref, base_f + 1), ref))
        else:
        w4, h4 = width(x4), height(x4)
        fw = (w8 + w4 - 1) // w4 if w4 else 1
        fh = (h8 + h4 - 1) // h4 if h4 else 1
        f = max(1, fw, fh)
        f_candidates.append((f, (i8, j8), None))

        for f, (oi, oj), ref in f_candidates:
        if f <= 0:
        continue
        x13 = upscale(x5, f)
        h13, w13 = height(x13), width(x13)
        max_row = len(x3) - h13
        max_col = len(x3[0]) - w13
        if max_row >= 0:
        min_row_off = 1
        max_row_off = len(x3) - h13 - 1
        if max_row_off >= min_row_off:
        row_range = range(min_row_off, max_row_off + 1)
        else:
        row_range = [clamp_offset(min_row_off, max_row)]
        else:
        row_range = [0]
        col_range = range(max_col + 1) if max_col >= 0 else [0]
        base_offset = (clamp_offset(oi, max_row), clamp_offset(oj, max_col))
        offsets = {base_offset}
        if ref is None:
        offsets.update((iv, jv) for iv in row_range for jv in col_range)
        if not offsets:
        offsets.add((0, 0))
        for off_i, off_j in offsets:
        x14 = shift(x13, (off_i, off_j))
        coords_map = {
        (i, j): v
        for v, (i, j) in x14
        if 0 <= i < len(x3) and 0 <= j < len(x3[0])
        }
        if not coords_map:
        continue
        if any(x3[i][j] == 4 for i, j in coords_map):
        continue
        if interior_map:
        matches = wrong = missing = 0
        for (pi, pj), expected in interior_map.items():
        got = coords_map.get((pi, pj))
        if got is None:
        missing += 1
        elif got == expected:
        matches += 1
        else:
        wrong += 1
        extra = len([1 for pos in coords_map if pos not in interior_map])
        score = matches * 200 - wrong * 500 - missing * 1000 - extra
        else:
        extra = len(coords_map)
        score = -extra
        if best_score is None or score > best_score:
        best_score, best_patch = score, x14

    # Fallback if no candidate evaluated (edge cases)
    return paint(x3, best_patch or [])
