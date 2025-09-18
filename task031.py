def p(j,A=enumerate):c,E=zip(*[(i,j)for i,r in A(j)for j,x in A(r)if x]);return[r[min(E):max(E)+1]for r in j[min(c):max(c)+1]]

