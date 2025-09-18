def p(g,L=len,R=range):
 h,w,I,J=L(g),L(g[0]),[],[]
 for r in R(h//2+1):
  for c in R(w):
   if g[r][c]==0:g[r][c]=g[-(r+1)][c];I+=[r];J+=[c]
   if g[-(r+1)][c]==0:g[-(r+1)][c]=g[r][c];I+=[h-(r+1)];J+=[c]
 for r in R(h):
  for c in R(w//2+1):
   if g[r][c]==0:g[r][c]=g[r][-(c+1)];I+=[r];J+=[c]
   if g[r][-(c+1)]==0:g[r][-(c+1)]=g[r][c];I+=[r];J+=[w-(c+1)]
 g=g[min(I):max(I)+1]
 g=[r[min(J):max(J)+1]for r in g]
 return g

