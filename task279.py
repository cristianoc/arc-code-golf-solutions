from collections import deque

def p(g):
    h,w=len(g),len(g[0])
    # Collect 4-connected components by color
    seen=[[0]*w for _ in range(h)]
    comps_by_color={}
    for i in range(h):
        for j in range(w):
            if not seen[i][j]:
                c=g[i][j]
                q=deque([(i,j)]); seen[i][j]=1; comp=[]
                while q:
                    x,y=q.popleft(); comp.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        u,v=x+dx,y+dy
                        if 0<=u<h and 0<=v<w and not seen[u][v] and g[u][v]==c:
                            seen[u][v]=1; q.append((u,v))
                comps_by_color.setdefault(c, []).append(set(comp))

    # Color 9 objects not touching the border
    comps9=[s for s in comps_by_color.get(9, []) if not any(x==0 or y==0 or x==h-1 or y==w-1 for x,y in s)]
    border_adj=set()
    for s in comps9:
        border_adj |= s
    # All neighbors of color-1 components; recolor those adjacent to any selected 9-comp
    out=[row[:] for row in g]
    comps1=comps_by_color.get(1, [])
    if comps1 and comps9:
        cells9=border_adj
        for s in comps1:
            adj=False
            for x,y in s:
                for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                    if (x+dx,y+dy) in cells9:
                        adj=True; break
                if adj: break
            if adj:
                for x,y in s:
                    out[x][y]=8
    return out

