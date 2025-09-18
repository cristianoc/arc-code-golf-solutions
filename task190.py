def p(g):
 R=range
 r=[x[:]for x in g]
 d=[(0,1),(1,0),(0,-1),(-1,0)]
 c=[(-1,-1),(-1,1),(1,1),(1,-1)]
 for i in R(10):
  for j in R(10):
   if g[i][j]and all(0<=i+x<10and 0<=j+y<10and g[i+x][j+y]==0for x,y in d):
    for t in c:
     x,y=i+t[0],j+t[1]
     if 0<=x<10and 0<=y<10and g[x][y]:
      a,b=-t[0],-t[1]
      for m in R(1,10):
       u,v=i+a*m,j+b*m
       if 0<=u<10and 0<=v<10:r[u][v]=g[i][j]
 return r

