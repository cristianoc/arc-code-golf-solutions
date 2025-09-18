# ARC Task 275

def p(j):
    A = min(len(j), len(j[0]))
    p, c = [r[:A]for r in j[:A]], [r[-A:]for r in j[-A:]]
    if any(max(r)==8 for r in p):p, c = c, p
    return[[p[y//A][x//A]*c[y%A][x%A]//8 for x in range(A * A)]for y in range(A * A)]
