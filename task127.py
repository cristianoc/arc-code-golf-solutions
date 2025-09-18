def p(g):
 R=range;Z=[r[:]for r in g];h,w=len(g),len(g[0])
 for r in R(1,h,4):
  for c in R(1,w,4):
   C=g[r][c]+5
   for y in R(3):
    for x in R(3):Z[r-1+y][c-1+x]=C
 return Z

