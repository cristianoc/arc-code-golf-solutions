def p(j):A=__import__('collections').Counter([x for R in j for x in R]).most_common(1);c=A[0][0];return[[A if A==c else 5 for A in R]for R in j]

