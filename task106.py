def p(j):A=lambda c:[*map(list,zip(*c[::-1]))];return[c+y for c,y in zip(j,A(j))]+[c+y for c,y in zip(A(A(A(j))),A(A(j)))]

