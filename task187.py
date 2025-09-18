def p(j):
 A,c,E=len(j),len(j[0]),range;k=[(W,l)for W in(0,A-1)for l in E(c)if j[W][l]<1]+[(W,l)for W in E(A)for l in(0,c-1)if j[W][l]<1]
 while k:
  W,l=k.pop()
  if j[W][l]<1:j[W][l]=3;k+=[(x,y)for x,y in((W+1,l),(W-1,l),(W,l+1),(W,l-1))if 0<=x<A and 0<=y<c and j[x][y]<1]
 for W in E(A):
  for l in E(c):
   if j[W][l]<1:j[W][l]=2
 return j

