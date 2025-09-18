def p(j):A=(j[3][3]<1)*6;[j[r].__setitem__(slice(A,A+3),j[r][3:6][::-1])for r in range(3)];return j

