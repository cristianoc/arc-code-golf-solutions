def p(g):
    I=[r[:] for r in g];H,W=len(I),len(I[0])
    # background color
    from collections import Counter
    vals=[v for r in I for v in r]
    bg=max(Counter(vals), key=Counter(vals).get)
    # 4-connected non-bg objects
    seen=[[False]*W for _ in range(H)]
    objs=[]
    for i in range(H):
        for j in range(W):
            if I[i][j]==bg or seen[i][j]:
                continue
            col=I[i][j]; q=[(i,j)]; seen[i][j]=True; cells=[]
            while q:
                a,b=q.pop(); cells.append((a,b))
                for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
                    x,y=a+di,b+dj
                    if 0<=x<H and 0<=y<W and not seen[x][y] and I[x][y]==col:
                        seen[x][y]=True; q.append((x,y))
            objs.append((col,cells))
    if not objs: return [[0]]
    # largest size
    s=max(len(c) for _,c in objs)
    # pick those with size s, order by leftmost
    cand=[(col,cells) for col,cells in objs if len(cells)==s]
    def leftmost(cells):
        return min(j for _,j in cells)
    cand.sort(key=lambda t:leftmost(t[1]))
    # dedupe colors preserving order
    colors=[]
    for col,_ in cand:
        if col not in colors: colors.append(col)
    n=len(colors)
    # build output: size x n with constant columns of each color
    return [[colors[j] for j in range(n)] for _ in range(s)]
