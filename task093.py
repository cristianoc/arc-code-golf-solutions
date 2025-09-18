def p(g):
    g=[r[:] for r in g]
    h,w=len(g),len(g[0])
    band=None; rows=[]; cols=[]
    for i in range(h):
        if len(set(g[i]))==1 and g[i][0]!=0:
            band=g[i][0]; rows.append(i)
    if band is None:
        for j in range(w):
            col=[g[i][j] for i in range(h)]
            if len(set(col))==1 and col[0]!=0:
                band=col[0]; cols.append(j)
        if band is not None:
            cols=[j for j in range(w) if all(g[i][j]==band for i in range(h))]
    else:
        rows=[i for i in range(h) if all(g[i][j]==band for j in range(w))]
    if band is None:
        band=5
    if rows:
        top=min(rows); bot=max(rows)
        above=[0]*w; below=[0]*w
        for i in range(h):
            for j in range(w):
                v=g[i][j]
                if v!=0 and v!=band:
                    if i<top: above[j]+=1
                    elif i>bot: below[j]+=1
        for j in range(w):
            for k in range(above[j]):
                r=top-1-k
                if 0<=r<h: g[r][j]=band
            for k in range(below[j]):
                r=bot+1+k
                if 0<=r<h: g[r][j]=band
        for i in range(h):
            for j in range(w):
                if g[i][j]!=0 and g[i][j]!=band and not (top<=i<=bot):
                    g[i][j]=0
        return g
    if cols:
        left=min(cols); right=max(cols)
        lc=[0]*h; rc=[0]*h
        for i in range(h):
            for j in range(w):
                v=g[i][j]
                if v!=0 and v!=band:
                    if j<left: lc[i]+=1
                    elif j>right: rc[i]+=1
        for i in range(h):
            for k in range(lc[i]):
                c=left-1-k
                if 0<=c<w: g[i][c]=band
            for k in range(rc[i]):
                c=right+1+k
                if 0<=c<w: g[i][c]=band
        for i in range(h):
            for j in range(w):
                if g[i][j]!=0 and g[i][j]!=band and not (left<=j<=right):
                    g[i][j]=0
        return g
    return g
