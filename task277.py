def p(j):
    h,w=len(j),len(j[0])
    # Find all 8-connected components of color 8
    vis=[[0]*w for _ in j]
    comps=[]
    for y in range(h):
        for x in range(w):
            if j[y][x]==8 and not vis[y][x]:
                q=[(y,x)];vis[y][x]=1;cur=[]
                while q:
                    i,k=q.pop();cur.append((i,k))
                    for di in (-1,0,1):
                        for dj in (-1,0,1):
                            if di==dj==0: continue
                            a,b=i+di,k+dj
                            if 0<=a<h and 0<=b<w and not vis[a][b] and j[a][b]==8:
                                vis[a][b]=1;q.append((a,b))
                comps.append(cur)
    if not comps:
        return [r[:] for r in j]
    # Group by normalized shape (sorted offsets from min i,j)
    def norm(c):
        mi=min(i for i,_ in c); mj=min(k for _,k in c)
        return tuple(sorted((i-mi,k-mj) for i,k in c))
    groups={}
    for c in comps:
        groups.setdefault(norm(c),[]).append(c)
    minc=min(len(v) for v in groups.values())
    cands=[c for k,v in groups.items() if len(v)==minc for c in v]
    # Tie-break by smallest (uppermost,leftmost)
    def key_ul(c):
        return (min(i for i,_ in c),min(k for _,k in c))
    chosen=min(cands,key=key_ul)
    # Paint: all 8 -> 1, chosen -> 2
    g=[r[:] for r in j]
    for i in range(h):
        for k in range(w):
            if g[i][k]==8:g[i][k]=1
    for i,k in chosen:g[i][k]=2
    return g

