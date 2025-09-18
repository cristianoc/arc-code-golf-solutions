p=lambda g,E=enumerate:[[v if(i and g[i-1][j]==v)+(i+1<len(g)and g[i+1][j]==v)+(j and r[j-1]==v)+(j+1<len(g)and r[j+1]==v)>1else 0 for j,v in E(r)]for i,r in E(g)]

