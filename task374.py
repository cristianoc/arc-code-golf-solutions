def p(j):
 A=len(j);c=len(j[0]);E=[]
 for k in range(A):
  for W in range(c):
   if j[k][W]==5:
    l=[(k,W)];j[k][W]=0;J=[]
    while l:
     a,C=l.pop();J+=[(a,C)]
     for e,K in((a+1,C),(a-1,C),(a,C+1),(a,C-1)):
      if 0<=e<A and 0<=K<c and j[e][K]==5:j[e][K]=0;l+=[(e,K)]
    E+=J,
 for J,w in zip(sorted(E,key=len),(2,4,1)):
  for a,C in J:j[a][C]=w
 return j

