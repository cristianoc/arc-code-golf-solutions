def p(j):
 A,c=len(j),len(j[0]);E=[A[:]for A in j]
 k,W=next((k,W)for k in range(A)for W in range(c)if j[k][W])
 for l,J in(-1,1),(1,-1):
  a,C=k,W
  while 1:
   for e in[0]*2:
    a+=l
    if 0<=a<A:E[a][C]=5
    else:break
   else:
    for e in[0]*2:
     C+=J
     if 0<=C<c:E[a][C]=5
     else:break
    else:continue
   break
 return E

