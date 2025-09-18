def p(j):
 A,c,E=j;k=6,4,0,0,0,1,3,1,0,0,0,4
 for W in range(len(A)):
  l=k[W%12]
  if l&1:A[W]=4
  if l&2:c[W]=4
  if l&4:E[W]=4
 return j

