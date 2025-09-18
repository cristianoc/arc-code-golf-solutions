# ARC Task 394

ZERO = 0

def _vperiod_grid(G):
    h, w = len(G), len(G[0])
    for p in range(1, h):
        ok = True
        for i in range(p, h):
        for j in range(w):
        if G[i][j]!=G[i - p][j]:
        ok = False
        break
        if not ok:
        break
        if ok:
        return p
    return h

def _hperiod_grid(G):
    h, w = len(G), len(G[0])
    for p in range(1, w):
        ok = True
        for j in range(p, w):
        for i in range(h):
        if G[i][j]!=G[i][j - p]:
        ok = False
        break
        if not ok:
        break
        if ok:
        return p
    return w

def _crop(I, r1, c1, r2, c2):
    return tuple(tuple(I[i][c1:c2 + 1]) for i in range(r1, r2 + 1))

def _hsplit(I, n):
    h, w = len(I), len(I[0])
    hh = h//n
    off = 1 if h % n != 0 else 0
    parts = []
    for i in range(n):
        si = hh * i + i * off
        if si + hh<=h:
        parts.append(_crop(I, si, 0, si + hh - 1, w - 1))
    return parts

def _vsplit(I, n):
    h, w = len(I), len(I[0])
    ww = w//n
    off = 1 if w % n != 0 else 0
    parts = []
    for i in range(n):
        sj = ww * i + i * off
        if sj + ww<=w:
        parts.append(_crop(I, 0, sj, h - 1, sj + ww - 1))
    return parts
 
def _palette(G):
    s = set()
    for r in G:
        s.update(r)
    return s


def solve_f9012d9b(I):
    h, w = len(I), len(I[0])
    # Collect all non - zero pixels with positions
    fg = [(I[i][j], (i, j)) for i in range(h) for j in range(w) if I[i][j]!=ZERO]

    # Identify zero region bounding box (if any)
    zeros = [(i, j) for i in range(h) for j in range(w) if I[i][j]==ZERO]
    r1 = c1 = r2 = c2 = None
    if zeros:
        r1 = min(i for i, _ in zeros)
        r2 = max(i for i, _ in zeros)
        c1 = min(j for _, j in zeros)
        c2 = max(j for _, j in zeros)
        zh = r2 - r1 + 1
        zw = c2 - c1 + 1

    best_v = None
    for n in range(2, h + 1):
        for part in _hsplit(I, n):
        if ZERO not in _palette(part):
        if best_v is None or len(part) > len(best_v):
        best_v = part
    best_h = None
    best_h_score = None
    for n in range(2, w + 1):
        for part in _vsplit(I, n):
        if ZERO not in _palette(part):
        w0 = len(part[0])
        ph_part = _hperiod_grid(part)
        pal_sz = len(_palette(part))
        score = (w0, 1 if ph_part>1 else 0, pal_sz)
        if best_h is None or score > best_h_score:
        best_h = part
        best_h_score = score
    if best_v is None:
        parts = _hsplit(I, 2)
        best_v = parts[0] if parts else I
    if best_h is None:
        parts = _vsplit(I, 2)
        best_h = parts[0] if parts else I

    pv = _vperiod_grid(best_v)
    ph = _hperiod_grid(best_h)

    # If zero hole exactly matches detected periods (non - trivial), choose the best adjacent patch
    if zeros:
        # Optionally refine horizontal period using fully non - zero boundary rows
        def _period1d(seq):
        n = len(seq)
        for p in range(1, n):
        ok = True
        for j in range(p, n):
        if seq[j]!=seq[j - p]:
        ok = False
        break
        if ok:
        return p
        return n
        ph_row = None
        for rr in (r1 - 1, r2 + 1):
        if 0<=rr<h and ZERO not in I[rr]:
        pr = _period1d(I[rr])
        if pr>1:
        ph_row = pr if ph_row is None else min(ph_row, pr)
        if ph_row and ph_row>1:
        ph = ph_row
        else:
        # As a fallback, infer a global row period from any non - uniform, zero - free row
        ph_global = None
        for rr in range(h):
        if ZERO not in I[rr]:
        pal = len(set(I[rr]))
        if pal>1:
        pr = _period1d(I[rr])
        if pr>1:
        ph_global = pr if ph_global is None else min(ph_global, pr)
        if ph_global and (zw % ph != 0) and (zw % ph_global == 0):
        ph = ph_global
        def rect_zero_free(rr, cc):
        if rr<0 or cc<0 or rr + zh>h or cc + zw>w:
        return None
        G = _crop(I, rr, cc, rr + zh - 1, cc + zw - 1)
        return G if ZERO not in _palette(G) else None

        # Collect candidate patches from vertical and horizontal neighbors
        candidates = []  # list of (patch, dir)
        if not (zh==1 and zw==1):
        for rr, cc, dd in ((r1 + pv, c1, 'V'), (r1 - pv, c1, 'V'), (r1, c1 + ph, 'H'), (r1, c1 - ph, 'H')):
        G = rect_zero_free(rr, cc)
        if G is not None:
        candidates.append((G, dd))

        # If we have multiple candidates, pick the one that appears most often elsewhere
        if candidates:
        # Score by local edge consistency around the zero region
        def edge_score(P):
        score = 0
        # source unknown; we compare P's context to the actual grid around target hole
        for i in range(zh):
        for j in range(zw):
        pi, pj = r1 + i, c1 + j
        v = P[i][j]
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ti, tj = pi + di, pj + dj
        if 0<=ti<h and 0<=tj<w:
        # ignore neighbor if it lies inside the zero hole
        if r1<=ti<=r2 and c1<=tj<=c2:
        continue
        if I[ti][tj]!=ZERO:
        # we expect the same relation in P: compare against the neighbor sampled from P
        si = i + di
        sj = j + dj
        if 0<=si<zh and 0<=sj<zw:
        if P[si][sj]==I[ti][tj]:
        score+=1
        return score

        def count_occurrences(P):
        cnt = 0
        for rr in range(h - zh + 1):
        for cc in range(w - zw + 1):
        if rr==r1 and cc==c1:
        continue
        block = _crop(I, rr, cc, rr + zh - 1, cc + zw - 1)
        if ZERO in _palette(block):
        continue
        if block==P:
        cnt+=1
        return cnt
        # Directional preference: favor the axis with larger detected period
        prefer_dir = 'H' if ph>pv else ('V' if pv>ph else None)
        def pref_score(dirflag):
        return 1 if prefer_dir and dirflag==prefer_dir else 0
        # Prefer direction with larger period, then edge consistency, then global frequency
        best_patch, _dir = max(candidates, key = lambda t: (pref_score(t[1]), edge_score(t[0]), count_occurrences(t[0])))
        return best_patch

    # neighbors of origin (8) then neighbors of those
    neigh8 = {(di, dj) for di in (-1, 0, 1) for dj in (-1, 0, 1) if (di, dj)!=(0, 0)}
    offs = {(a + u, b + v) for a, b in neigh8 for u, v in neigh8}

    # Deterministic nearest - first ordering of scaled offsets
    scaled = sorted(((di * pv, dj * ph) for di, dj in offs), key = lambda t: (abs(t[0])+abs(t[1]), t))

    # If there is a zero region, try to fill it from nearest periodic copies without overwriting
    if zeros:
        # Recompute bounds locally to mirror original flow
        r1 = min(i for i, _ in zeros)
        r2 = max(i for i, _ in zeros)
        c1 = min(j for _, j in zeros)
        c2 = max(j for _, j in zeros)
        zh = r2 - r1 + 1
        zw = c2 - c1 + 1
        # Direct per - cell projection using periods: try horizontal first, then vertical
        fill = {}
        for ti in range(r1, r2 + 1):
        for tj in range(c1, c2 + 1):
        val = None
        for oi, oj in ((0, ph), (0, -ph), (pv, 0), (-pv, 0)):
        si, sj = ti + oi, tj + oj
        if 0<=si<h and 0<=sj<w and I[si][sj]!=ZERO:
        val = I[si][sj]
        break
        if val is not None:
        fill[(ti, tj)]=val
        if len(fill)==zh * zw:
        return tuple(tuple(fill[(r1 + i, c1 + j)] for j in range(zw)) for i in range(zh))

        # Fallback: gather from many offsets (nearest - first)
        fill = {}
        # Bias to pull from the horizontally - aligned neighbor first when horizontal period exists
        preferred = (0, -ph)
        fill_offsets = ([preferred] if preferred not in scaled else []) + [t for t in scaled if t!=preferred]
        for di, dj in fill_offsets:
        for v, (i, j) in fg:
        ti, tj = i + di, j + dj
        if r1<=ti<=r2 and c1<=tj<=c2:
        if (ti, tj) not in fill:
        fill[(ti, tj)]=v
        if len(fill)==zh * zw:
        # Build output directly
        return tuple(tuple(fill[(r1 + i, c1 + j)] for j in range(zw)) for i in range(zh))

    # Fallback: shift foreground by each offset and paint, then crop
    obj = [(v, (i + di, j + dj)) for di, dj in scaled for v, (i, j) in fg]
    O = [list(r) for r in I]
    for v, (i, j) in obj:
        if 0<=i<h and 0<=j<w:
        O[i][j]=v
    painted = tuple(tuple(r) for r in O)

    if not zeros:
        return painted
    return _crop(painted, r1, c1, r2, c2)

def p(g):
    try:
        G = tuple(tuple(r) for r in g)
        R = solve_f9012d9b(G)
        return [list(r) for r in R] if isinstance(R, tuple) else R
    except Exception:
        # Guard: on any unexpected error, echo input as lists
        return [list(r) for r in g]
