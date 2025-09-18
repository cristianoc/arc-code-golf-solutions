j=lambda A:[[A[c][E]for c in range(len(A))]for E in range(len(A[0]))]
def h(A,c,E):
 if A[c][E]!=2or A[c][E+1]!=2:return
 for k in range(max(0,c-1),min(len(A),c+2)):
  for W in range(max(0,E-1),min(len(A[0]),E+3)):
   if A[k][W]!=2:A[k][W]=3
def f(A):
 for c in range(len(A)):
  for E in range(len(A[0])-1):h(A,c,E)
def p(A):f(A);A=j(A);f(A);return j(A)

