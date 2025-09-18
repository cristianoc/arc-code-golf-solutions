# ARC Task 074

def solve_3631a71a(I):
    # Guard empty input
    if not I or not I[0]:
        return tuple()
    H, W = len(I), len(I[0])
    # Replace 9->0
    A = [[0 if v == 9 else v for v in row] for row in I]
    # Element - wise max with its transpose over the largest square
    s = min(H, W)
    AT = list(map(list, zip(*A)))
    M = [[max(A[i][j], AT[i][j]) for j in range(s)] for i in range(s)]
    if s <= 2:
        return tuple(map(tuple, M))
    # Overlay mirrored cropped region using 0 as transparent background
    # Include row index 1 as well (needed for some edge cases),
    # but keep column start at 2 to avoid overfilling the left band.
    V = [row[2:s][::-1] for row in M[1:s]]
    O = [row[:] for row in M]
    for i, row in enumerate(V, start = 1):
        for j, v in enumerate(row, start = 2):
        if v != 0:
        O[i][j] = v
    return tuple(map(tuple, O))


def p(g):
    # Iterate the transformation until convergence.
    cur = tuple(tuple(row) for row in g)
    for _ in range(256):
        nxt = solve_3631a71a(cur)
        if nxt == cur:
        break
        cur = nxt
    return [list(row) for row in cur]
