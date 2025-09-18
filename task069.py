def p(g,E=enumerate):
 P=[]
 for r,R in E(g):
  for c,C in E(R):
   if C not in[0,8]:P+=[[r,c,C]];g[r][c]=0
 Z=P[0][:];P=[[x[0]-Z[0],x[1]-Z[1],x[2]]for x in P]
 for r,R in E(g):
  for c,C in E(R):
   if C==8:
    g[r][c]=Z[2]
    for x in P:g[r+x[0]][c+x[1]]=x[2]
 return g

