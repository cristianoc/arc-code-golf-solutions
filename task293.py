j=lambda A:[A[0]]*len(A)if A[0]else A
c=lambda E:[[E[y][x]for y in range(len(E))]for x in range(len(E[0]))]
k=lambda E:[j(A)for A in E]
p=lambda E:c(k(c(E)))if k(E)==E else k(E)

