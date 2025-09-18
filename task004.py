def p(j,A=enumerate):
 c=[[0]*len(j[0])for _ in j]
 for E in set(sum(j,[]))-{0}:
  k=[(J,a)for J,r in A(j)for a,x in A(r)if x==E];W,l=max(J for J,_ in k),max(a for _,a in k)
  for J,a in k:c[J][a+(J<W and a<l)]=E
 return c
