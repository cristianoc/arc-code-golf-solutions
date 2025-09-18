# ARC Task 018

"""
Task 018 – Optimization reminder (moved from TODO_changed_programs.txt)
- Direct solver (no DSL) now at ~2.3KB with 100% accuracy.
- Consider further golfing to increase score:
    * Inline helpers
    * Compress D4 transforms
    * Reduce temporary variables
"""

def dc(G):
    cnt = {}
    for r in G:
        for v in r:
        if v:
        cnt[v]=cnt.get(v, 0)+1
    return max(cnt, key = cnt.get) if cnt else 0

def o(G):
    H, W = len(G), len(G[0])
    vis = [[False]*W for _ in range(H)]
    objs = []
    for i in range(H):
        for j in range(W):
        if G[i][j] and not vis[i][j]:
        q = [(i, j)]
        vis[i][j]=True
        cells = []
        pal = set()
        while q:
        a, b = q.pop()
        v = G[a][b]
        pal.add(v)
        cells.append((a, b, v))
        for da, db in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        x, y = a + da, b + db
        if 0<=x<H and 0<=y<W and G[x][y] and not vis[x][y]:
        vis[x][y]=True
        q.append((x, y))
        objs.append({'c':cells, 'p':pal})
    return objs

T = (
    lambda i, j:(i, j),
    lambda i, j:(j, -i),
    lambda i, j:(-i, -j),
    lambda i, j:(-j, i),
    lambda i, j:(-i, j),
    lambda i, j:(i, -j),
    lambda i, j:(j, i),
    lambda i, j:(-j, -i),
)

def mt(G, cs):
    H, W = len(G), len(G[0])
    hi = max(i for i, _, _ in cs)+1
    wj = max(j for _, j, _ in cs)+1
    out = []
    for si in range(H - hi + 1):
        for sj in range(W - wj + 1):
        for i, j, v in cs:
        if G[si + i][sj + j]!=v:
        break
        else:
        out.append((si, sj))
    return out

def s(G, si, sj, cs):
    for i, j, v in cs:
        G[si + i][sj + j]=v

def p(g):
    if not g:return g
    G = [r[:] for r in g]
    d = dc(G)
    ns = [x for x in o(G) if len(x['c'])>3 and len(x['p'])>1]
    for x in ns:
        B = x['c']
        A = [(i, j, v) for i, j, v in B if v!=d]
        if not A:continue
        S = set()
        for f in T:
        F = [(f(i, j)[0], f(i, j)[1], v) for i, j, v in B]
        mi = min(i for i, _, _ in F)
        mj = min(j for _, j, _ in F)
        F = [(i - mi, j - mj, v) for i, j, v in F]
        a = [(f(i, j)[0], f(i, j)[1], v) for i, j, v in A]
        a = [(i - mi, j - mj, v) for i, j, v in a]
        ai = min(i for i, _, _ in a)
        aj = min(j for _, j, _ in a)
        m = [(i - ai, j - aj, v) for i, j, v in a]
        k = tuple(sorted((i, j, v) for i, j, v in m))
        if k in S:continue
        S.add(k)
        for si, sj in mt(G, m):
        s(G, si - ai, sj - aj, F)
    for x in ns:
        if d in x['p']:
        for a, b, _ in x['c']:
        G[a][b]=0
    return G
