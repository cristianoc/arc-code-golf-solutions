# ARC Task 304

def p(j, A = range(9), c = range(3)):
    E, k = __import__('collections').Counter(j[0]+j[1]+j[2]).most_common(1)[0][0], [[0 for _ in A]for _ in A]
    for W, l in[(W, l)for l in c for W in c if j[W][l]==E]:
    for J in A:k[3 * W + J%3][3 * l + J//3]=j[J%3][J//3]
    return k
