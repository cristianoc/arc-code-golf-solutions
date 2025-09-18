# ARC Task 170

def p(j):
    h, w = len(j), len(j[0])
    from collections import Counter, deque
    bg = Counter(v for r in j for v in r).most_common(1)[0][0]
    vis = [[0]*w for _ in range(h)]
    comps = []
    for i in range(h):
    for k in range(w):
    if vis[i][k] or j[i][k]==bg: continue
    q = deque([(i, k)])
    vis[i][k]=1
    pts = [(i, k)]
    while q:
        x, y = q.popleft()
        for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
        if dx==dy==0: continue
        a, b = x + dx, y + dy
        if 0<=a<h and 0<=b<w and not vis[a][b] and j[a][b]!=bg:
        vis[a][b]=1
        q.append((a, b))
        pts.append((a, b))
    xs = [x for x, _ in pts]
    ys = [y for _, y in pts]
    comps.append((pts, (min(xs), min(ys), max(xs), max(ys))))
    comps.sort(key = lambda t: len(t[0]))
    small, large = comps[0], comps[-1]
    (si, sj, ei, ej)=small[1]
    (LI, LJ, LEI, LEJ)=large[1]
    sg = [row[sj:ej + 1] for row in j[si:ei + 1]]
    lg = [row[LJ:LEJ + 1] for row in j[LI:LEI + 1]]
    fw = len(lg[0])//len(sg[0])
    # downscale lg by factor fw and zero - mask positions
    mask = [[1 if lg[r * fw][c * fw]==0 else 0 for c in range(len(sg[0]))] for r in range(len(sg))]
    for r in range(len(sg)):
    for c in range(len(sg[0])):
    if mask[r][c]: sg[r][c]=0
    return sg
