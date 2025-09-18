# ARC Task 192

def p(g, L = len, R = range):
    h, w = L(g), L(g[0])
    # Dominant non - zero color P; outputs use palette {0, P}
    f = sum(g, [])
    cnt = {}
    for v in f:
    if v: cnt[v]=cnt.get(v, 0)+1
    if not cnt: return g
    P = max(cnt, key = lambda k:(cnt[k], k))
    # Mark bounding boxes of all 4 - connected P - components
    fill = [[0]*w for _ in g]
    seen = [[0]*w for _ in g]
    for r in R(h):
    for c in R(w):
    if g[r][c]==P and not seen[r][c]:
    q = [(r, c)]
    seen[r][c]=1
    r0 = r1 = r
    c0 = c1 = c
    while q:
    y, x = q.pop()
    if y<r0:r0 = y
    if y>r1:r1 = y
    if x<c0:c0 = x
    if x>c1:c1 = x
    for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
    yy = y + dy
    xx = x + dx
    if 0<=yy<h and 0<=xx<w and not seen[yy][xx] and g[yy][xx]==P:
    seen[yy][xx]=1
    q.append((yy, xx))
    for y in R(r0, r1 + 1):
    for x in R(c0, c1 + 1):
    fill[y][x]=1
    # Render: keep P; inside bbox snap attached impurities; else 0
    o = [[0]*w for _ in g]
    for r in R(h):
    for c in R(w):
    v = g[r][c]
    if v==P:
    o[r][c]=P
    elif v!=0:
    if fill[r][c] and ((r>0 and g[r - 1][c]==P) or (r + 1<h and g[r + 1][c]==P) or (c>0 and g[r][c - 1]==P) or (c + 1<w and g[r][c + 1]==P)):
    o[r][c]=P
    else:
    o[r][c]=0
    else:
    o[r][c]=0
    return o
