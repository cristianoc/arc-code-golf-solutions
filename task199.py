def p(j,A=enumerate):
 for c,E in A(j):
  for k,W in A(E):
   if W and W^4:
    j[c+1][k]=W
    for l in range(c+1):j[l][k&1::2]=[4]*len(j[l][k&1::2])
    return j

