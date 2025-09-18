def p(j):
 A=enumerate;c=next
 E=lambda k,W:k<1or j[k-1][W]<1or k>2and j[k-1][W]==4and j[k-2][W]>0
 (k,W),(l,J),(a,l),l=[divmod(i,13)for i,v in A(sum(j,[]))if v==4]
 C=c(u for r in zip(*j)if 4not in r for u in r if u)
 e=c(i for i,r in A(j)if any(u==C and E(i,v)for v,u in A(r)))
 K=c(i for i,r in A(zip(*j))if any(u==C and E(v,i)for v,u in A(r)))
 for w in range(a-k-1):
  for L in range(J-W-1):j[k+w+1][[J-L-1,W+L+1][j[k+1][W]==C]],j[e+w][K+L]=j[e+w][K+L],0
 return[r[W:J+1]for r in j[k:a+1]]

