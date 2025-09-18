# ARC Task 253

def p(j):
    A = len(j)-1
    c = [0]*16
    for E in range(A):
    for k in range(A):
    if(W:=j[E][k])and j[E + 1][k]==W and j[E][k + 1]==W:c[0]=c[4]=c[1]=W
    if W and j[E + 1][k]==W and j[E + 1][k + 1]==W:c[8]=c[12]=c[13]=W
    if W and j[E][k + 1]==W and j[E + 1][k + 1]==W:c[2]=c[3]=c[7]=W
    if(l:=j[E + 1][k + 1])and j[E + 1][k]==l and j[E][k + 1]==l:c[11]=c[14]=c[15]=l
    return[c[E:E + 4]for E in(0, 4, 8, 12)]
