# ARC Task 060

def p(j):
    A = len(j[0])
    c = int((A - 1)/2)
    E = enumerate
    for(k, W)in E(j):
        if max(W)>0:
    for l in range(c):j[k][l]=j[k][0]
    j[k][A - l-1]=j[k][A - 1]
        j[k][c]=5
    return j
