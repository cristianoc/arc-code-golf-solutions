def p(j):
 for A in j:
  for c in range(len(A)-2):
   if A[c]&A[c+2]:A[c+1]=2
 return j

