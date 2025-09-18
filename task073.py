def p(j):
 A=[o[:]for o in j]
 for c in range(5):
  for E in range(5):
   if j[E][c]==1:A[E][c]=0;A[4][c]=1
 return A

