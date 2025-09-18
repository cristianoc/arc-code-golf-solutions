def f(j,A,c,E,k):
 W=j[A][c]
 if W==0:return
 if not sum(j[A][c+i]==W for i in(1,-1))==sum(j[A+i][c]==W for i in(1,-1))==1:return
 l,J,p,a=2*(j[A+1][c]==W)-1,2*(j[A][c+1]==W)-1,c,A
 if j[A+l][c+J]==W:return
 while 1<=p<k-1and 1<=a<E-1:a-=l;p-=J;j[a][p]=j[A+2*l][c+2*J]
def p(j):
 E,k=len(j),len(j[0])
 for A in range(1,E-1):
  for c in range(1,k-1):f(j,A,c,E,k)
 return j

