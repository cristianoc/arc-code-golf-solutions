from collections import Counter, deque

def p(g):
    h,w=len(g),len(g[0])
    bg=Counter(v for r in g for v in r).most_common(1)[0][0]
    out=[row[:] for row in g]
    seen=[[0]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if g[i][j]!=bg and not seen[i][j]:
                col=g[i][j]
                q=deque([(i,j)]); seen[i][j]=1; comp=[]
                while q:
                    x,y=q.popleft(); comp.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        u,v=x+dx,y+dy
                        if 0<=u<h and 0<=v<w and not seen[u][v] and g[u][v]==col:
                            seen[u][v]=1; q.append((u,v))
                cval=2 if len(comp)==6 else 1
                for x,y in comp:
                    out[x][y]=cval
    return out

