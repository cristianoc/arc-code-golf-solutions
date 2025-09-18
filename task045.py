def p(j):
	for A in j:
		for c in{*A}-{0}:
			E=A.index(c);k=len(A)-A[::-1].index(c)
			for W in range(E,k):
				if~A[W]:A[W]=c
	return j

