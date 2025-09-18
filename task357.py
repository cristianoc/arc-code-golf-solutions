def p(g,R=range,L=len):
 h,w=L(g),L(g[0])
 g=[[8 for i in r]for r in g]
 C=[i for i in range(w)]
 C+=C[::-1][1:-1]
 while L(C)<h:C+=C[:]
 for r in R(h):g[-(r+1)][C[r]]=1
 return g

