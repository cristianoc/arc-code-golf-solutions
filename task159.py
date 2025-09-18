F = False
T = True

ZERO = 0
ONE = 1
TWO = 2
THREE = 3

def _bg_color(G):
    flat = [v for r in G for v in r]
    return max(set(flat), key=flat.count)

def _components_nonbg_univalued_diag(G):
    # components of non-background, single color, 8-neighborhood
    bg = _bg_color(G)
    h, w = len(G), len(G[0])
    seen = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if seen[i][j] or G[i][j]==bg:
                continue
            color = G[i][j]
            q=[(i,j)]
            seen[i][j]=True
            cur=[]
            while q:
                a,b = q.pop()
                cur.append((a,b,color))
                for da in (-1,0,1):
                    for db in (-1,0,1):
                        if da==0 and db==0:
                            continue
                        na,nb = a+da,b+db
                        if 0<=na<h and 0<=nb<w and not seen[na][nb] and G[na][nb]==color:
                            seen[na][nb]=True
                            q.append((na,nb))
            comps.append(cur)
    return comps

def _normalize(obj):
    mi = min(i for i,_,_ in obj)
    mj = min(j for _,j,_ in obj)
    return [(i-mi, j-mj, v) for i,j,v in obj]

def _upscale(obj, k):
    if k == 1:
        return list(obj)
    out=[]
    for i,j,v in obj:
        for di in range(k):
            for dj in range(k):
                out.append((i*k+di, j*k+dj, v))
    return out

def solve_6b9890af(I):
    h, w = len(I), len(I[0])

    # Bounding box of all color-2 cells
    pos2 = [(i,j) for i in range(h) for j in range(w) if I[i][j]==TWO]
    if not pos2:
        return tuple(tuple(r) for r in I)
    i0 = min(i for i,_ in pos2)
    j0 = min(j for _,j in pos2)
    i1 = max(i for i,_ in pos2)
    j1 = max(j for _,j in pos2)

    # Crop subgrid
    sub = [list(I[i][j0:j1+1]) for i in range(i0, i1+1)]
    sub_h, sub_w = len(sub), len(sub[0])

    # Smallest non-bg, univalued, diag component in full I
    comps = _components_nonbg_univalued_diag(I)
    if not comps:
        return tuple(tuple(r) for r in sub)
    small = min(comps, key=lambda c: len(c))

    # Scale factor from subgrid width
    s = (sub_w) // 3
    obj = _normalize(_upscale(small, s))
    # shift by UNITY (1,1)
    obj = [(i+1, j+1, v) for i,j,v in obj]

    # Paint into subgrid
    for i,j,v in obj:
        if 0<=i<sub_h and 0<=j<sub_w:
            sub[i][j] = v

    return tuple(tuple(r) for r in sub)

def p(g):
    I = tuple(tuple(r) for r in g)
    R = solve_6b9890af(I)
    return [list(r) for r in R]

