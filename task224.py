def p(g,L=len,R=range,M=max,N=min):
 h,w,y,x=L(g),L(g[0]),[],[]
 C=[C for C in set(sum(g,[])) if C not in [0,5]][0]
 for r in R(h):
  for c in R(w):
   if g[r][c]==5:y+=[r];x+=[c]
 for r in R(h):
  for c in R(w):
   if r in [N(y)+1,M(y)-1] and N(x)+1<=c<=M(x)-1:g[r][c]=C
   if c in [N(x)+1,M(x)-1] and N(y)+1<=r<=M(y)-1:g[r][c]=C
 return g

