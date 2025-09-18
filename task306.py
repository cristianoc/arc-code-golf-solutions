def solve_c444b776(I):
    H,W=len(I),len(I[0])
    G=[list(r) for r in I]
    # Divider lines: full row/col of same non-zero color
    row_lines=[i for i in range(H) if G[i][0]!=0 and all(G[i][j]==G[i][0] for j in range(W))]
    col_lines=[j for j in range(W) if G[0][j]!=0 and all(G[i][j]==G[0][j] for i in range(H))]
    if not row_lines and not col_lines:
        return I
    # Segments between divider lines (exclusive of the line)
    row_segs=[]; prev=0
    for rl in row_lines:
        if prev<rl: row_segs.append((prev,rl))
        prev=rl+1
    if prev<H: row_segs.append((prev,H))
    if not row_segs: row_segs=[(0,H)]
    col_segs=[]; prev=0
    for cl in col_lines:
        if prev<cl: col_segs.append((prev,cl))
        prev=cl+1
    if prev<W: col_segs.append((prev,W))
    if not col_segs: col_segs=[(0,W)]
    def find_seg(segs,x):
        for k,(s,e) in enumerate(segs):
            if s<=x<e: return k
        return -1
    cells=[]
    for i in range(H):
        for j in range(W):
            v=G[i][j]
            if v==0 or i in row_lines or j in col_lines:
                continue
            ri=find_seg(row_segs,i); cj=find_seg(col_segs,j)
            if ri==-1 or cj==-1: continue
            li=i-row_segs[ri][0]; lj=j-col_segs[cj][0]
            cells.append((ri,cj,li,lj,v))
    for ri,cj,li,lj,v in cells:
        for rs,re in row_segs:
            ti=rs+li
            if not (rs<=ti<re): continue
            for cs,ce in col_segs:
                tj=cs+lj
                if not (cs<=tj<ce): continue
                if ti==(row_segs[ri][0]+li) and tj==(col_segs[cj][0]+lj):
                    continue
                if G[ti][tj]==0:
                    G[ti][tj]=v
    return tuple(tuple(r) for r in G)

def p(g):
    G=tuple(tuple(r) for r in g)
    R=solve_c444b776(G)
    return [list(r) for r in R]

