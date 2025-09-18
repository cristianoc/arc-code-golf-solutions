def _most_color(grid):
    cnt={}
    for r in grid:
        for v in r:
            cnt[v]=cnt.get(v,0)+1
    return max(cnt, key=cnt.get)

def solve_cbded52d(I):
    H,W=len(I),len(I[0])
    bg=_most_color(I)
    G=[list(r) for r in I]
    singles=[]  # (i,j,color)
    for i in range(H):
        for j in range(W):
            v=I[i][j]
            if v==bg: continue
            same=False
            for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
                ni,nj=i+di,j+dj
                if 0<=ni<H and 0<=nj<W and I[ni][nj]==v:
                    same=True; break
            if not same:
                singles.append((i,j,v))
    # For every ordered pair sharing row or column, color the center cell
    for a_i,a_j,a_c in singles:
        for b_i,b_j,_ in singles:
            if a_i==b_i:
                cj=(min(a_j,b_j)+max(a_j,b_j)+1)//2  # ceil midpoint
                ci=a_i
            elif a_j==b_j:
                ci=(min(a_i,b_i)+max(a_i,b_i)+1)//2
                cj=a_j
            else:
                continue
            if 0<=ci<H and 0<=cj<W:
                G[ci][cj]=a_c
    return tuple(tuple(r) for r in G)

def p(g):
    G=tuple(tuple(r) for r in g)
    R=solve_cbded52d(G)
    return [list(r) for r in R]

