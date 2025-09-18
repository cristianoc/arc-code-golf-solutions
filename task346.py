# ARC Task 346

from collections import*
def p(j):
    for A in range(0, len(j)-3 + 1, 1):
    for c in range(0, len(j[0])-3 + 1, 1):
    E = j[A:A + 3]
    E = [R[c:c + 3]for R in E]
    k = [i for s in E for i in s]
    W = Counter(k).most_common(1)
    if min(k)>0and W[0][1]==8:return[[E[1][1]]]
