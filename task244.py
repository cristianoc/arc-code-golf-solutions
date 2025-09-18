# ARC Task 244

def p(g, V = range):R, C = len(g), len(g[0])
G = [-1]+[i for i in V(R)if len({*g[i]})==1]+[R]
z = [-1]+[j for j in V(C)if len({g[i][j]for i in V(R)})==1]+[C]
o = [[g[a + 1][c + 1]for c, d in zip(z, z[1:])if c + 1<d - 1]for a, b in zip(G, G[1:])if a + 1<b - 1]
return[o[::-1]for o in o]
