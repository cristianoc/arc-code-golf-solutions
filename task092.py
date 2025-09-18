def p(g,L=len,R=range):
 H,W=L(g),L(g[0]);o=[r[:]for r in g]
 for i in R(H):
  x=C=None
  for j in R(W):
   if g[i][j]:
    if x is not None and g[i][j]==C:
     for k in R(x+1,j):o[i][k]=C
    x=j;C=g[i][j]
 for j in R(W):
  x=C=None
  for i in R(H):
   if g[i][j]:
    if x is not None and g[i][j]==C:
     for k in R(x+1,i):o[k][j]=C
    x=i;C=g[i][j]
 return o

