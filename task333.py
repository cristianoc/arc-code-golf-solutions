THREE = 3

def solve_d43fd935(I):
    H, W = len(I), len(I[0])

    def mostcolor(grid):
        values = [v for r in grid for v in r]
        # most frequent value
        from collections import Counter
        return Counter(values).most_common(1)[0][0]

    def asindices(grid):
        return {(i, j) for i in range(len(grid)) for j in range(len(grid[0]))}

    def dneighbors(loc):
        i,j = loc
        return {(i-1,j),(i+1,j),(i,j-1),(i,j+1)}

    def objects(grid):
        bg = mostcolor(grid)
        objs = []
        occupied = set()
        h, w = len(grid), len(grid[0])
        for loc in asindices(grid):
            if loc in occupied:
                continue
            val = grid[loc[0]][loc[1]]
            if val == bg:
                continue
            obj = {(val, loc)}
            cands = {loc}
            while cands:
                neighborhood = set()
                for cand in cands:
                    v = grid[cand[0]][cand[1]]
                    if v == val:
                        obj.add((v, cand))
                        occupied.add(cand)
                        neighborhood |= {(i, j) for i, j in dneighbors(cand) if 0 <= i < h and 0 <= j < w}
                cands = neighborhood - occupied
            # Use a regular set; no need for frozenset
            objs.append(set(obj))
        return objs

    def toindices(patch):
        if not patch:
            return set()
        first = next(iter(patch))
        if isinstance(first, tuple) and len(first) == 2 and isinstance(first[1], tuple):
            return {idx for _, idx in patch}
        return set(patch)

    def uppermost(patch):
        return min(i for i,_ in toindices(patch))
    def lowermost(patch):
        return max(i for i,_ in toindices(patch))
    def leftmost(patch):
        return min(j for _,j in toindices(patch))
    def rightmost(patch):
        return max(j for _,j in toindices(patch))
    def height(patch):
        return lowermost(patch) - uppermost(patch) + 1
    def width(patch):
        return rightmost(patch) - leftmost(patch) + 1
    def center(patch):
        return (uppermost(patch) + height(patch)//2, leftmost(patch) + width(patch)//2)

    def hmatching(a, b):
        ai = {i for i,_ in toindices(a)}
        bi = {i for i,_ in toindices(b)}
        return len(ai & bi) > 0
    def vmatching(a, b):
        aj = {j for _,j in toindices(a)}
        bj = {j for _,j in toindices(b)}
        return len(aj & bj) > 0
    def manhattan(a, b):
        A = toindices(a); B = toindices(b)
        return min(abs(ai-bi)+abs(aj-bj) for ai,aj in A for bi,bj in B)
    def adjacent(a, b):
        return manhattan(a, b) == 1

    def shift(patch, d):
        di,dj = d
        if not patch:
            return patch
        first = next(iter(patch))
        if isinstance(first, tuple) and len(first) == 2 and isinstance(first[1], tuple):
            return {(v,(i+di,j+dj)) for v,(i,j) in patch}
        return {(i+di, j+dj) for i,j in patch}

    def connect(a, b):
        ai, aj = a
        bi, bj = b
        si = min(ai, bi)
        ei = max(ai, bi) + 1
        sj = min(aj, bj)
        ej = max(aj, bj) + 1
        if ai == bi:
            return {(ai, j) for j in range(sj, ej)}
        elif aj == bj:
            return {(i, aj) for i in range(si, ei)}
        elif bi - ai == bj - aj:
            return {(i, j) for i, j in zip(range(si, ei), range(sj, ej))}
        elif bi - ai == aj - bj:
            return {(i, j) for i, j in zip(range(si, ei), range(ej - 1, sj - 1, -1))}
        return set()

    def color(obj):
        return next(iter(obj))[0]

    def recolor(value, patch):
        return {(value, idx) for idx in toindices(patch)}

    def ofcolor(grid, value):
        return {(i, j) for i in range(H) for j in range(W) if grid[i][j] == value}

    def paint(grid, obj):
        G = [list(r) for r in grid]
        for v,(i,j) in obj:
            if 0 <= i < H and 0 <= j < W:
                G[i][j] = v
        # Return list-of-lists directly
        return G

    def _anchor_to(source, destination):
        ci, cj = center(source)
        src_idx = list(toindices(source))
        si = {i for i,_ in src_idx}
        sj = {j for _,j in src_idx}
        di = {i for i,_ in toindices(destination)}
        dj = {j for _,j in toindices(destination)}
        if vmatching(source, destination):
            inter = sj & dj
            aj = min(inter, key=lambda x: abs(x - cj)) if inter else cj
            candidates = [loc for loc in src_idx if loc[1] == aj]
            if not candidates:
                candidates = sorted(src_idx, key=lambda loc: (abs(loc[1] - aj), abs(loc[0] - ci)))
            ai, aj = candidates[0]
            return (ai, aj)
        else:
            inter = si & di
            ai = min(inter, key=lambda x: abs(x - ci)) if inter else ci
            candidates = [loc for loc in src_idx if loc[0] == ai]
            if not candidates:
                candidates = sorted(src_idx, key=lambda loc: (abs(loc[0] - ai), abs(loc[1] - cj)))
            ai, aj = candidates[0]
            return (ai, aj)

    def gravitate(source, destination):
        si, sj = center(source)
        di, dj = center(destination)
        i, j = (0, 0)
        if vmatching(source, destination):
            i = 1 if si < di else -1
        else:
            j = 1 if sj < dj else -1
        gi, gj = (i, j)
        c = 0
        src = toindices(source)
        dst = toindices(destination)
        while not adjacent(src, dst) and c < 42:
            c += 1
            gi += i
            gj += j
            src = shift(src, (i, j))
        return (gi - i, gj - j)

    # Pipeline reimplemented without DSL combinators
    objs = objects(I)
    target = ofcolor(I, THREE)
    to_draw = []
    for o in objs:
        if color(o) == THREE:
            continue
        if not (hmatching(o, target) or vmatching(o, target)):
            continue
        anch = _anchor_to(o, target)
        di, dj = gravitate(o, target)
        path = connect(anch, (anch[0] + di, anch[1] + dj))
        to_draw.extend(recolor(color(o), path))
    return paint(I, to_draw)

def p(g):
    tg = tuple(tuple(row) for row in g)
    # solve_d43fd935 now returns list-of-lists already
    return solve_d43fd935(tg)
