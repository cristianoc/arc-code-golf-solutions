def p(j,A=enumerate):
 for c,E in A(j):
  for k,W in A(E):
   if c<len(j)//2:j[c][k]=j[-(c+1)][k]
 return j

