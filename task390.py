def p(g):
 # work on a mutable copy
 G=[row[:] for row in g]
 h=len(G); w=len(G[0])
 # locate extremal rows/cols containing 2s
 cols=[c for r in G for c,v in enumerate(r) if v==2]
 if not cols:return G
 L=min(cols); R=max(cols)
 rows=[i for i,r in enumerate(G) if 2 in r]
 top=min(rows); bot=max(rows)
 # detect presence of horizontal edges: full 2-band from L..R
 hs=[i for i,row in enumerate(G) if all(row[c]==2 for c in range(L,R+1))]
 has_h=bool(hs)
 if has_h:
  # top/bottom horizontal edge rows specifically
  top_h=min(hs); bot_h=max(hs)
  for r in range(top_h+1,bot_h):
   # collect interior 5s between vertical sides
   f=[c for c in range(L+1,R) if G[r][c]==5]
   if not f:continue
   # remove originals
   for c in f:G[r][c]=0
   # mirror each 5 to nearest horizontal edge
   dt=r-top_h; db=bot_h-r
   if dt<=db:
    tr=top_h-dt
    if 0<=tr<h:
     for c in f:G[tr][c]=5
   else:
    tr=bot_h+db
    if 0<=tr<h:
     for c in f:G[tr][c]=5
 else:
  # vertical sides only: mirror horizontally across nearest side
  for r in range(top,bot+1):
   f=[c for c in range(L+1,R) if G[r][c]==5]
   if not f:continue
   for c in f:
    dl=c-L; dr=R-c
    if dl<=dr:
     tc=L-dl
    else:
     tc=R+dr
    if 0<=tc<w:G[r][tc]=5
    G[r][c]=0
 return G
