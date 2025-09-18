def p(g):h,w=len(g),len(g[0]);return[[1if g[i][j]and all(g[i+a][j+b]==0for a,b in[(-1,0),(1,0),(0,-1),(0,1)]if 0<=i+a<h and 0<=j+b<w)else g[i][j]for j in range(w)]for i in range(h)]

