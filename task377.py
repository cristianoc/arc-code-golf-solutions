def p(g,L=len,R=range):
 h,w=L(g),L(g[0])
 c,C=0,[]
 for r in R(L(g)):
  K=[g[r][0]]
  for i in R(L(g[r])-1):
   if g[r][i+1]!=g[r][i]:K+=[g[r][i+1]]
  if L(K)>c:c=L(K);C=K[:]
 g=[C[:] for _ in R(L(C))]
 for r in R(L(g)//2):
  for c in R(r,L(g[0])-r-1):
   g[r][c]=g[r][r]
   g[-(r+1)][c]=g[-(r+1)][r]
 return g

