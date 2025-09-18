def p(g,V=range):
 r=[d[:]for d in g]
 v=set()
 for i in V(len(g)-2):
  for j in V(len(g[0])):
   if g[i][j]and(i,j)not in v:
    c=g[i][j]
    if all(g[i+k][j]==c for k in V(3)):
     a=j
     while a<len(g[0])and all(g[i+k][a]==c for k in V(3)):
      for k in V(3):v.add((i+k,a))
      a+=1
     for x in V(j,a):
      if(x-j)%2==1:r[i+1][x]=0
 return r

