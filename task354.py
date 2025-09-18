def p(j):
 A=range
 c=[x[:]for x in j]
 def d(E,k,W):
  if 0<=E<10and 0<=k<10and c[E][k]==5:c[E][k]=W;[d(E+a,k+b,W)for a,b in[(-1,0),(1,0),(0,-1),(0,1)]]
 [[d(E,k,j[0][k])for E in A(1,10)if c[E][k]==5]for k in A(10)if j[0][k]]
 return c

