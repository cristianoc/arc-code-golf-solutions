# ARC Task 197

def p(j):
    A = next((c for c in j if 0 not in c), None)
    if not A:return j
    c = []
    [c.append(W)for W in A if W not in c]
    for(E, k)in enumerate(j):
        if 0 in k and any(k):
    W = []
    [W.append(c)for c in k if c not in W and c]
    if len(c)==len(W):l = dict(zip(c, W))
    j[E]=[l[c]for c in A]
    return j
