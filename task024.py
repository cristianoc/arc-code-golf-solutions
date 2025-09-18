def p(g,E=enumerate):Z={c for R in g for c,v in E(R)if v==2};return[[1 if 1 in R else 3 if 3 in R else 2 if v<1and c in Z else v for c,v in E(R)]for R in g]

