j=lambda A:[[A[E][c]for E in range(len(A))]for c in range(len(A[0]))]
def J(A):c=[A for(A,c)in enumerate(A)if any(c)];return c[0],c[-1]
def p(A):
	c,E=J(A);k,W=J(j(A))
	def F(l,J,a,C):A[l][J],A[a][C]=A[a][C],A[l][J]
	F(c+1,k+1,E+1,W+1);F(c+1,W-1,E+1,k-1);F(E-1,k+1,c-1,W+1);F(E-1,W-1,c-1,k-1);return A

