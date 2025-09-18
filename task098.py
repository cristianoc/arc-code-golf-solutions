p=lambda g:[[x if any(g[i+di][j+dj]==0 for di,dj in[(0,1),(1,0),(0,-1),(-1,0)]if 0<=i+di<len(g)and 0<=j+dj<len(g[0]))and x!=0 else 0 for j,x in enumerate(r)]for i,r in enumerate(g)]

