# ARC Task 255

def p(g):
    H, W = len(g), len(g[0])
    E = [[not g[i][j]and all((not(0<=i + di<H and 0<=j + dj<W))or not g[i + di][j + dj] for di in(-1, 0, 1) for dj in(-1, 0, 1) if di or dj) for j in range(W)] for i in range(H)]
    h = [0]*W
    R = []
    for i in range(H):
    for j in range(W):h[j]=E[i][j]and h[j]+1
    for L in range(W):
    m = h[L]
    if not m:continue
    for r in range(L, W):
    if not h[r]:break
    m = min(m, h[r])
    for k in range(1, m + 1):R.append((i - k + 1, L, i, r, (r - L + 1)*k))
    F = lambda x:x[3]-x[1]+1
    G = lambda x:x[2]-x[0]+1
    R.sort(key = lambda r:(-r[4], r[0], r[1]))
    if not R:return [[*r]for r in g]
    bh = next((r for r in R if F(r)>G(r)), 0)
    bv = next((r for r in R if G(r)>F(r)), 0)
    I = (bh and bv and (bh if F(bh)>G(bv) else bv if F(bh)<G(bv) else (bh if bh[4]>=bv[4] else bv))) or bh or bv or R[0]
    o = [[*r]for r in g]
    def P(a):
    for i in range(a[0], a[2]+1):o[i][a[1]:a[3]+1]=[3]*F(a)
    V = lambda a, b:a[1]<=b[3]and b[1]<=a[3]and a[0]<=b[2]and b[0]<=a[2]
    m = "vh"[F(I)<=G(I)]
    T = lambda a:(a[1]==0 or a[3]==W - 1)if m=='h'else(a[0]==0 or a[2]==H - 1)
    A = lambda a:((a[3]+1==I[1] or a[1]-1==I[3])and a[0]<=I[2]and a[2]>=I[0])if m=='h'else((a[2]+1==I[0] or a[0]-1==I[2])and a[1]<=I[3]and a[3]>=I[1])
    def K(a):
    if m=='h':
    for r in (a[0]-1, a[2]+1):
    if 0<=r<H and 3 in o[r][a[1]:a[3]+1]:return 0
    else:
    for c in (a[1]-1, a[3]+1):
    if 0<=c<W and 3 in[*zip(*o[a[0]:a[2]+1])][c]:return 0
    return 1
    P(I)
    C = [I]
    while 1:
    for r in sorted(R, key = lambda r:(not T(r), -r[4], r[0], r[1])):
    if (F, G)[m>'h'](r)<5 or not K(r) or not A(r) or any(V(r, c)for c in C):continue
    P(r)
    C+=[r]
    break
    else:break
    return o
