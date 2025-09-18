# ARC Task 028

def p(g, m = max):e, a = m(map(m, g[:5])), m(map(m, g[-5:]))
return[[(r in(0, 2, 7, 9)or c%9<1)*(e*(r<5)+a*(r>4))for c in range(10)]for r in range(10)]
