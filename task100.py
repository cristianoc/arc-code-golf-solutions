def p(g,E=enumerate,M=max,N=min):
 d={k:{0:[],1:[]} for k in set(sum(g,[]))}
 for(r,R)in E(g):
  for(c,C)in E(R):d[C][0]+=[r];d[C][1]+=[c]
 Z=[];del d[0]
 for k in d:X=d[k];Z+=[[(M(X[0])-N(X[0])+1)*(M(X[1])-N(X[1])+1),k,len(X[1])]]
 C=sorted(Z)[-1][1]
 return[[C,C],[C,C]]

