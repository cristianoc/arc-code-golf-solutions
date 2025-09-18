from collections import deque

def p(g):
    h,w=len(g),len(g[0])
    o=[row[:] for row in g]
    seen=[[0]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if g[i][j]==6 and not seen[i][j]:
                # BFS to get one 4-connected component of color 6
                q=deque([(i,j)]); comp=[]; seen[i][j]=1
                while q:
                    x,y=q.popleft(); comp.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        u,v=x+dx,y+dy
                        if 0<=u<h and 0<=v<w and not seen[u][v] and g[u][v]==6:
                            seen[u][v]=1; q.append((u,v))
                mi=min(x for x,_ in comp); ma=max(x for x,_ in comp)
                mj=min(y for _,y in comp); mb=max(y for _,y in comp)
                # Outer box border in 3 (expanded by 1)
                for y in range(mj-1, mb+2):
                    if 0<=mi-1<h and 0<=y<w: o[mi-1][y]=3
                    if 0<=ma+1<h and 0<=y<w: o[ma+1][y]=3
                for x in range(mi-1, ma+2):
                    if 0<=x<h and 0<=mj-1<w: o[x][mj-1]=3
                    if 0<=x<h and 0<=mb+1<w: o[x][mb+1]=3
                s=set(comp)
                # Fill inner bbox (excluding the object) with 4
                for x in range(mi, ma+1):
                    for y in range(mj, mb+1):
                        if (x,y) not in s: o[x][y]=4
    return o
