from collections import Counter, deque

def p(j):
    # Preprocess: treat color 5 as 0 for background detection
    A = [[0 if v == 5 else v for v in r] for r in j]
    h, w = len(A), len(A[0])
    bg = Counter(v for r in A for v in r).most_common(1)[0][0]

    # Find 4-connected, univalued components excluding background; store normalized shapes with colors
    seen = [[False]*w for _ in range(h)]
    comps = []  # (color, shape as tuple of (di,dj))
    for i in range(h):
        for k in range(w):
            if seen[i][k]:
                continue
            seen[i][k] = True
            if A[i][k] == bg:
                continue
            col = A[i][k]
            q = deque([(i, k)])
            coords = {(i, k)}
            while q:
                ci, cj = q.popleft()
                for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
                    ni, nj = ci+di, cj+dj
                    if 0 <= ni < h and 0 <= nj < w and not seen[ni][nj]:
                        seen[ni][nj] = True
                        if A[ni][nj] == col:
                            coords.add((ni, nj))
                            q.append((ni, nj))
            mi = min(x for x,_ in coords); mj = min(y for _,y in coords)
            # Use a stable, hashable key without frozenset: sorted tuple of relative coords
            norm = tuple(sorted((x - mi, y - mj) for x, y in coords))
            comps.append((col, norm))

    # Build 9x9 template border with specific gaps and cross points
    H = W = 9
    ones = {(i,0) for i in range(H)} | {(i,W-1) for i in range(H)} | {(0,j) for j in range(W)} | {(H-1,j) for j in range(W)}
    for j2 in (2, W-3):
        ones.discard((0, j2)); ones.discard((H-1, j2))
    for i2 in (2, H-3):
        ones.discard((i2, 0)); ones.discard((i2, W-1))
    ones |= {(4,1), (4,W-2), (1,4), (H-2,4)}

    # Group 4-connected shapes among ones by normalized shape -> sorted UL positions
    seen_t = [[False]*W for _ in range(H)]
    shp_pos = {}
    for i in range(H):
        for k in range(W):
            if seen_t[i][k] or (i,k) not in ones:
                continue
            q = deque([(i, k)])
            seen_t[i][k] = True
            coords = {(i, k)}
            while q:
                ci, cj = q.popleft()
                for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
                    ni, nj = ci+di, cj+dj
                    if 0 <= ni < H and 0 <= nj < W and not seen_t[ni][nj] and (ni, nj) in ones:
                        seen_t[ni][nj] = True
                        coords.add((ni, nj))
                        q.append((ni, nj))
            mi = min(x for x,_ in coords); mj = min(y for _,y in coords)
            # Normalize shape as a sorted tuple of relative coords (hashable, order-independent)
            shp = tuple(sorted((x - mi, y - mj) for x, y in coords))
            shp_pos.setdefault(shp, []).append((mi, mj))
    for shp in shp_pos:
        shp_pos[shp].sort()

    # Paint components onto template using their colors; background is 5
    O = [[5]*W for _ in range(H)]
    for col, shp in comps:
        pos = shp_pos.get(shp)
        if not pos:
            continue
        ui, uj = pos.pop(0)
        for di, dj in shp:
            O[ui+di][uj+dj] = col
    return O
