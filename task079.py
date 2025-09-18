def p(g):
    I=[r[:] for r in g];H,W=len(I),len(I[0])
    vals=[v for r in I for v in r]
    bg=max(set(vals),key=vals.count)
    seen=[[False]*W for _ in range(H)]
    objs=[]
    for i in range(H):
        for j in range(W):
            if I[i][j]==bg or seen[i][j]:
                continue
            col=I[i][j];q=[(i,j)];cells=[];seen[i][j]=True
            while q:
                a,b=q.pop();cells.append((a,b))
                for di,dj in ((1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)):
                    x,y=a+di,b+dj
                    if 0<=x<H and 0<=y<W and not seen[x][y] and I[x][y]==col:
                        seen[x][y]=True;q.append((x,y))
            objs.append((col,cells))
    from collections import Counter
    cnt=Counter(c for c,_ in objs)
    if not cnt: return I
    target=max(cnt.keys(),key=lambda c:(cnt[c],c))
    cand=[cells for c,cells in objs if c==target]
    def bbox(cells):
        is_=[i for i,_ in cells]; js=[j for _,j in cells]
        return min(is_),min(js),max(is_),max(js)
    ti,tj,bi,bj=min((bbox(c),) for c in cand)[0]
    return [row[tj:bj+1] for row in I[ti:bi+1]]
