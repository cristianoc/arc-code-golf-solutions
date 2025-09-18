def p(j,A=enumerate,c=range(11)):
 E=0;k=[[0 if(i+1)%4>0and(j+1)%4>0 else 5 for i in c]for j in c];W={'00':0,'01':0,'02':0,'10':0,'11':0,'12':0,'20':0,'21':0,'22':0}
 for l,J in A(j):
  for a,C in A(J):
   if C>0and C!=5:E=int(C);W[str(l//4)+str(a//4)]+=1
 e=max(W.values())
 for l,J in A(k):
  for a,C in A(J):
   if C==0and W[str(l//4)+str(a//4)]==e:k[l][a]=E
 return k

