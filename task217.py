def p(j,A=range(9)):c,E=next(i for i,r in enumerate(j)if sum(r))//3*3,next(i for i in A if sum(j[y][i]for y in A))//3*3;return[[j[c+y%3][E+x%3]*bool(j[c+y//3][E+x//3])for x in A]for y in A]

