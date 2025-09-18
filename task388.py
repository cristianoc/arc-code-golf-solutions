def p(g):R=range;n=len(g);c={j for i in R(n)for j in R(n)if g[i][j]};m=[[8if g[i][j]==0and j in c else g[i][j]for j in R(n)]for i in R(n)];return[[m[i%n][j%n]for j in R(2*n)]for i in R(2*n)]

