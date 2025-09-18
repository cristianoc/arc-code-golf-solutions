def p(j,A=range):
 c=len(j);E=len(j[0]);p=[J[:]for J in j]
 for k in A(E):
  W=[J for J in A(c)if j[J][k]];l=len(W)//2
  for J in A(l):p[W[-1-J]][k]=8
 return p

