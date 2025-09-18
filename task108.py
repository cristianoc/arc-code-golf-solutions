def p(j,A=range):c,E=len(j),len(j[0]);k=[[max(j[y][x],j[y][x+1],j[y+1][x],j[y+1][x+1])for x in A(0,E,2)]for y in A(0,c,2)];return[[k[y//4][x//4]for x in A(2*E)]for y in A(2*c)]

