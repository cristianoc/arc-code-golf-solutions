L=len
R=range
def p(g):
 h,w=L(g),L(g[0])
 for r in R(h):
  for c in R(w):
   if g[r][c]==2:
    for i,j in[[1,1],[-1,-1],[-1,1],[1,-1]]:g[i+r][j+c]=4
   if g[r][c]==1:
    for i,j in[[0,1],[0,-1],[-1,0],[1,0]]:g[i+r][j+c]=7
 return g

