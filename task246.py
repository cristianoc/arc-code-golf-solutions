def p(j):
 A=range
 c=[J[:]for J in j]
 for E in A(len(j)):
  for k in A(len(j[0])):
   if j[E][k]==2:W,l=E,k
   if j[E][k]==3:J,a=E,k
 C=1if a>l else-1
 for k in A(l+C,a+C,C):c[W][k]=8
 C=1if J>W else-1
 for E in A(W+C,J,C):c[E][a]=8
 return c

