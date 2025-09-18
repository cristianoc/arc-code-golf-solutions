def p(g,u=range):n=len(g);m=len(g[0]);r=[i for i in u(n)if len(set(g[i]))==1];c=[j for j in u(m)if len(set(g[i][j]for i in u(n)))==1];b=next(x for i in u(n)for j,x in enumerate(g[i])if i not in r and j not in c);return[[b]*(len(c)+1)for _ in u(len(r)+1)]

