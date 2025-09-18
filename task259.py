def p(j,A=range):
 c,E=len(j),len(j[0]);k,W,l,J=c,0,E,0
 for a in A(c):
  for C in A(E):
   if j[a][C]-1:
    if a<k:k=a
    if a>W:W=a
    if C<l:l=C
    if C>J:J=C
 return[[x-(x==1)for x in r[l:J+1]]for r in j[k:W+1]]

