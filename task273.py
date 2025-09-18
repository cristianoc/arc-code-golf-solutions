def p(j):
    H,W=len(j),len(j[0])
    # 1) positions of color 4
    F=[(y,x) for y in range(H) for x in range(W) if j[y][x]==4]
    # 2) connect pairs sharing row/col
    seg=set()
    for a in range(len(F)):
        y1,x1=F[a]
        for b in range(a,len(F)):
            y2,x2=F[b]
            if y1==y2:
                for x in range(min(x1,x2),max(x1,x2)+1): seg.add((y1,x))
            if x1==x2:
                for y in range(min(y1,y2),max(y1,y2)+1): seg.add((y,x1))
    # 3) underfill those segments with -1 only on background cells
    flat=[v for r in j for v in r]
    bg=max(set(flat),key=flat.count)
    G=[r[:] for r in j]
    for y,x in seg:
        if 0<=y<H and 0<=x<W and G[y][x]==bg: G[y][x]=-1
    # 4) 4-connected components of non-bg
    seen=[[0]*W for _ in j]
    comps=[]
    for y in range(H):
        for x in range(W):
            if G[y][x]!=bg and not seen[y][x]:
                q=[(y,x)];seen[y][x]=1;cur=[]
                while q:
                    i,k=q.pop();cur.append((i,k))
                    for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
                        a,b=i+di,k+dj
                        if 0<=a<H and 0<=b<W and not seen[a][b] and G[a][b]!=bg:
                            seen[a][b]=1;q.append((a,b))
                comps.append(cur)
    # 5) inbox fill with 2
    for c in comps:
        ys=[i for i,_ in c]; xs=[k for _,k in c]
        y0,y1=min(ys)+1,max(ys)-1; x0,x1=min(xs)+1,max(xs)-1
        for i in range(y0,y1+1):
            for k in range(x0,x1+1):
                if 0<=i<H and 0<=k<W: G[i][k]=2
    # 6) replace -1 with 0
    for i in range(H):
        for k in range(W):
            if G[i][k]==-1:G[i][k]=0
    return G

