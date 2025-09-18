def _normalize_pixels(pxs):
    if not pxs:
        return set()
    is_ = [i for _, (i, j) in pxs]
    js = [j for _, (i, j) in pxs]
    mi, mj = min(is_), min(js)
    return {(v, (i - mi, j - mj)) for v, (i, j) in pxs}

def _upscale_pixels(pxs, f):
    return {
        (v, (i * f + di, j * f + dj))
        for v, (i, j) in pxs
        for di in range(f)
        for dj in range(f)
    }

def _outbox_indices(coords):
    if not coords:
        return set()
    is_ = [i for i, _ in coords]
    js = [j for _, j in coords]
    si, sj = min(is_) - 1, min(js) - 1
    ei, ej = max(is_) + 1, max(js) + 1
    return (
        {(i, sj) for i in range(si, ei + 1)}
        | {(i, ej) for i in range(si, ei + 1)}
        | {(si, j) for j in range(sj, ej + 1)}
        | {(ei, j) for j in range(sj, ej + 1)}
    )

def _occurrences(G, pattern):
    if not pattern or not G or not G[0]:
        return set()
    H, W = len(G), len(G[0])
    pat = _normalize_pixels(pattern)
    pis = [i for _, (i, j) in pat]
    pjs = [j for _, (i, j) in pat]
    ph, pw = max(pis) + 1, max(pjs) + 1
    occs = set()
    for si in range(-ph + 1, H):
        for sj in range(-pw + 1, W):
            ok = True
            any_in_bounds = False
            for v, (i, j) in pat:
                ti, tj = si + i, sj + j
                if 0 <= ti < H and 0 <= tj < W:
                    any_in_bounds = True
                    if G[ti][tj] != v:
                        ok = False
                        break
                else:
                    if v != 0:
                        ok = False
                        break
            if ok and any_in_bounds:
                occs.add((si, sj))
    return occs

def _components_8(G, bg):
    if not G or not G[0]:
        return []
    H, W = len(G), len(G[0])
    vis = [[False] * W for _ in range(H)]
    comps = []
    dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    from collections import deque
    for i in range(H):
        for j in range(W):
            if vis[i][j] or G[i][j] == bg:
                continue
            q = deque([(i, j)])
            vis[i][j] = True
            comp = []
            while q:
                a, b = q.popleft()
                comp.append((G[a][b], (a, b)))
                for di, dj in dirs:
                    ni, nj = a + di, b + dj
                    if 0 <= ni < H and 0 <= nj < W and not vis[ni][nj] and G[ni][nj] != bg:
                        vis[ni][nj] = True
                        q.append((ni, nj))
            comps.append(comp)
    return comps

def solve_447fd412(I):
    from collections import Counter
    if not I or not I[0]:
        return []
    cnt_bg = {}
    for r in I:
        for v in r:
            cnt_bg[v] = cnt_bg.get(v, 0) + 1
    bg = max(cnt_bg, key=cnt_bg.get)
    comps = _components_8(I, bg)
    if not comps:
        return I
    comps.sort(key=lambda c: len({v for v, _ in c}), reverse=True)
    target = comps[0]
    norm = _normalize_pixels(target)
    cnt = Counter(v for v, _ in target)
    mc = max(cnt.items(), key=lambda kv: (kv[1], -kv[0]))[0]
    placements = []
    for f in (1, 2, 3):
        scaled = _upscale_pixels(norm, f)
        # Prefer matching minority colors; fallback to majority skeleton
        minz = {(v, ij) for v, ij in scaled if v != mc}
        occs = set()
        coords = set()
        if minz:
            coords = {ij for _, ij in minz}
            pattern = minz | {(0, ij) for ij in _outbox_indices(coords)}
            occs = _occurrences(I, pattern)
        if not occs:
            maj = {(v, ij) for v, ij in scaled if v == mc}
            if not maj:
                continue
            coords = {ij for _, ij in maj}
            pattern = maj | {(0, ij) for ij in _outbox_indices(coords)}
            occs = _occurrences(I, pattern)
        if not occs:
            continue
        ui = min(i for i, _ in coords)
        uj = min(j for _, j in coords)
        for oi, oj in occs:
            di, dj = oi - ui + 1, oj - uj + 1
            placements.append({(v, (i + di, j + dj)) for v, (i, j) in scaled})
    if not placements:
        return I
    H, W = len(I), len(I[0])
    O = [list(r) for r in I]
    for v, (i, j) in set().union(*placements):
        if 0 <= i < H and 0 <= j < W:
            O[i][j] = v
    return tuple(tuple(r) for r in O)

def p(g):
    R = solve_447fd412(g)
    return [list(r) for r in R]
