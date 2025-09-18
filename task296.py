def p(j):
 A=[[0]*3,[0]*3,[0]*3]
 for c in range(16):E,k=c//8%2*-2+c//2%2,c//4%2*-2+c%2;A[E][k]=max(A[E][k],j[E][k])
 return A

