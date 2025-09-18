# ARC Task 345

def p(j):
    for A in range(len(j[0])):
        if j[-1][A]==2:
        c = 0
        for E in range(len(j)):
    if j[-(E + 1)][A + c]==5:c+=1
    j[-E][A + c]=2
        j[-(E + 1)][A + c]=2
    return j
