E=enumerate
L=len
def p(g):
 f=sum(g,[])
 C=sorted([[f.count(c),c] for c in set(f) if c>0])
 P=[[x,y] for y,r in E(g) for x,c in E(r) if c==C[-1][1]]
 f=sum(P,[]);x=f[::2];y=f[1::2]
 X=g[min(y):max(y)+1]
 X=[r[min(x):max(x)+1][:] for r in X]
 if L(X)<3:
  if X[0].count(0)>0:X=[[0,0,0]]+X
  else:X=X+[[0,0,0]]
 if L(X[0])<3:
  if [X[0][0],X[1][0],X[2][0]].count(0)>0:X=[[0]+r for r in X]
  else:X=[r+[0] for r in X]
 X=[[C[0][1] if c==0 else c for c in r] for r in X]
 return X