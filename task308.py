def _most_color(grid):
    cnt={}
    for r in grid:
        for v in r:
            cnt[v]=cnt.get(v,0)+1
    return max(cnt, key=cnt.get)

def solve_c8cbb738(I):
    # Group all foreground cells by color (excluding background),
    # compute each group's bbox, create a canvas sized to the max (h,w),
    # and center each normalized group onto the canvas.
    H,W=len(I),len(I[0])
    bg=_most_color(I)
    pos_by_color={}
    for i in range(H):
        for j in range(W):
            v=I[i][j]
            if v==bg: continue
            pos_by_color.setdefault(v,[]).append((i,j))
    if not pos_by_color:
        return I
    dims={}
    for v,ps in pos_by_color.items():
        is_=[p[0] for p in ps]; js=[p[1] for p in ps]
        h=max(is_)-min(is_)+1; w=max(js)-min(js)+1
        dims[v]=(h,w)
    mh=max(h for h,_ in dims.values()); mw=max(w for _,w in dims.values())
    O=[[bg]*mw for _ in range(mh)]
    for v,ps in pos_by_color.items():
        is_=[p[0] for p in ps]; js=[p[1] for p in ps]
        mi,mj=min(is_),min(js)
        h,w=dims[v]
        offi=(mh-h)//2; offj=(mw-w)//2
        for i,j in ps:
            ni=i-mi+offi; nj=j-mj+offj
            if 0<=ni<mh and 0<=nj<mw:
                O[ni][nj]=v
    return tuple(tuple(r) for r in O)

def p(g):
    G=tuple(tuple(r) for r in g)
    R=solve_c8cbb738(G)
    return [list(r) for r in R]

