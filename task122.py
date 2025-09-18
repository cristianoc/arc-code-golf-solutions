def p(g,L=len,R=range):
 for r in R(L(g)):
  for c in R(L(g[0])):
   if g[r][c]==2:
    if g[r+1].count(3)>1: #Horizontal
     for y in R(3):
      for x in R(3):
       g[r+y][c+x+2]= g[r+y][c+x]
       if g[r+y][c+x]==2 and x<2:g[r+y][c+x]=0
     return g
    else:
     for y in R(3):
      for x in R(3):
       g[r+y+2][c+x]=g[r+y][c+x]
       if g[r+y][c+x]==2 and y<2:g[r+y][c+x]=0
     return g

