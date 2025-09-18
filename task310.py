# ARC Task 310

from collections import Counter
def p(m):
    c = Counter(e for r in m for e in r if e).most_common()
    if not c:return[]
    l = c[-1][0]
    O = p=-1
    for i, r in enumerate(m):
    if l in r:
    if O<0:O = i
    p = i
    S = U=-1
    for i in range(len(m[0])):
    if any(m[j][i]==l for j in range(O, p + 1)):
    if S<0:S = i
    U = i
    return[r[S:U + 1]for r in m[O:p + 1]]
