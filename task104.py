def p(g):
 e,Z=[],[g[0][0],g[0][2],g[2][2],g[2][0]]
 for r in [[3,0],[0,3]]:
  for i in range(4):e+=[sum([[c]*4 for c in r],[])+[0]]
 e+=[[0]*len(e[0])]
 for i in range(Z.index(3)):e=[list(r) for r in list(zip(*e[::-1]))]
 return e

