ZERO=0
EIGHT=8


def solve_b782dc8a(I):
    # Multi-source BFS that alternates two non-background colors while
    # spreading only through zeros. Existing non-zero cells remain.
    h,w=len(I),len(I[0])
    G=[list(r) for r in I]
    from collections import deque
    vals={v for r in I for v in r}
    bg=EIGHT if EIGHT in vals else _most_color(I)
    colors=sorted(v for v in vals if v not in (bg, ZERO))
    if len(colors)!=2:
        return I
    a,b=colors
    q=deque()
    seen=[[False]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if G[i][j] in (a,b):
                q.append((i,j,G[i][j]))
                seen[i][j]=True
    if not q:
        return I
    while q:
        i,j,c=q.popleft()
        for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni,nj=i+di,j+dj
            if 0<=ni<h and 0<=nj<w and not seen[ni][nj]:
                if G[ni][nj]==ZERO:
                    nc=b if c==a else a
                    G[ni][nj]=nc
                    seen[ni][nj]=True
                    q.append((ni,nj,nc))
                else:
                    seen[ni][nj]=True
    return tuple(tuple(r) for r in G)

def p(g):
    G=tuple(tuple(r) for r in g)
    R=solve_b782dc8a(G)
    return [list(r) for r in R]
