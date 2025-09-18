# ARC Task 311

def solve_c9e6f938(I):
    # Mirror each row horizontally by appending its reverse (list - of - lists)
    return [list(row) + list(reversed(row)) for row in I]

def p(g):
    try:
        out = solve_c9e6f938(g)
        if isinstance(out, tuple):
        return [list(r) for r in out]
        return out
    except Exception:
        return [list(r) for r in g]
