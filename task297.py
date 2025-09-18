def p(j):
 A,c=len(j),len(j[0]);E=j[0]*20
 for k in range(2,A):j[k]=[E[k-2]for _ in range(c)]
 return j

