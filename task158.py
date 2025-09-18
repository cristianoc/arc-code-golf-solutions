# ARC Task 158

F = False
T = True

ZERO = 0
ONE = 1
TWO = 2
THREE = 3
FOUR = 4
FIVE = 5
SIX = 6
SEVEN = 7
EIGHT = 8
NINE = 9

def _bg_color(G):
    flat = [v for r in G for v in r]
    return max(set(flat), key = flat.count)

def _most_color_in_obj(obj):
    vals = [v for _, _, v in obj]
    return max(set(vals), key = vals.count)

def _components_nonbg_anycolor_diag(G):
    # components of non - background pixels (mixing colors), 8 - neighborhood
    bg = _bg_color(G)
    h, w = len(G), len(G[0])
    seen = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
        if seen[i][j] or G[i][j]==bg:
        continue
        q = [(i, j)]
        seen[i][j]=True
        cur = []
        while q:
        a, b = q.pop()
        cur.append((a, b, G[a][b]))
        for da in (-1, 0, 1):
        for db in (-1, 0, 1):
        if da==0 and db==0:
        continue
        na, nb = a + da, b + db
        if 0<=na<h and 0<=nb<w and not seen[na][nb] and G[na][nb]!=bg:
        seen[na][nb]=True
        q.append((na, nb))
        comps.append(cur)
    return comps

def _normalize(obj):
    mi = min(i for i, _, _ in obj)
    mj = min(j for _, j, _ in obj)
    return [(i - mi, j - mj, v) for i, j, v in obj]

def _upscale(obj, k):
    if k == 1:
        return list(obj)
    out = []
    for i, j, v in obj:
        for di in range(k):
        for dj in range(k):
        out.append((i * k + di, j * k + dj, v))
    return out

def _dims(obj):
    h = max(i for i, _, _ in obj) + 1 if obj else 0
    w = max(j for _, j, _ in obj) + 1 if obj else 0
    return h, w

def _vmirror(obj):
    h, w = _dims(obj)
    return [(i, w - 1-j, v) for i, j, v in obj]

def _hmirror(obj):
    h, w = _dims(obj)
    return [(h - 1-i, j, v) for i, j, v in obj]

def _cmirror(obj):
    # Match DSL: vmirror ∘ dmirror ∘ vmirror
    return _vmirror(_dmirror(_vmirror(obj)))

def _dmirror(obj):
    return [(j, i, v) for i, j, v in obj]

def _occurrences(G, pattern):
    # pattern must be normalized (starts at 0, 0)
    if not pattern:
        return []
    h, w = len(G), len(G[0])
    ph, pw = _dims(pattern)
    out = []
    for si in range(h - ph + 1):
        for sj in range(w - pw + 1):
        ok = True
        for i, j, v in pattern:
        if G[si + i][sj + j] != v:
        ok = False
        break
        if ok:
        out.append((si, sj))
    return out

def solve_6aa20dc0(I):
    comps = _components_nonbg_anycolor_diag(I)
    if not comps:
        return tuple(tuple(r) for r in I)

    # Pick component with maximum number of colors
    def num_colors(c):
        return len(set(v for _, _, v in c))
    best = None
    best_nc = -1
    for c in comps:
        nc = num_colors(c)
        if nc > best_nc:
        best_nc = nc
        best = c

    base_obj = _normalize(best)

    # Transforms: identity, vmirror, hmirror, cmirror (180 deg), dmirror (transpose)
    transforms = [
        lambda o:o,
        _vmirror,
        _hmirror,
        _cmirror,
        _dmirror,
    ]
    scales = [1, 2, 3]

    O = [list(r) for r in I]

    bg = _bg_color(I)
    for k in scales:
        scaled = _upscale(base_obj, k)
        scaled = _normalize(scaled)
        for t in transforms:
        obj = _normalize(t(scaled))
        if not obj:
        continue
        main = _most_color_in_obj(obj)
        minority = [(i, j, v) for i, j, v in obj if v != main]
        minority = _normalize(minority)
        # Precompute minority coordinate set and bounding box dims
        mcoords = {(i, j) for i, j, _ in minority}
        ph, pw = _dims(minority)
        for si, sj in _occurrences(I, minority):
        # Require that all non - minority cells within the bounding box are background
        ok_box = True
        for di in range(ph):
        for dj in range(pw):
        if (di, dj) in mcoords:
        continue
        if I[si + di][sj + dj] != bg:
        ok_box = False
        break
        if not ok_box:
        break
        if not ok_box:
        continue
        for i, j, v in obj:
        a, b = si + i, sj + j
        if 0<=a<len(O) and 0<=b<len(O[0]):
        O[a][b] = v

    return tuple(tuple(r) for r in O)

def p(g):
    I = tuple(tuple(r) for r in g)
    R = solve_6aa20dc0(I)
    return [list(r) for r in R]
