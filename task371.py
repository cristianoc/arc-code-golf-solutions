def p(j,A=enumerate):
 c,E=zip(*((i,j)for i,r in A(j)for j,W in A(r)if W))
 for k,W in((0,0),(-1,0),(1,0),(0,-1),(0,1)):j[sum(c)//2+k][sum(E)//2+W]=3
 return j

