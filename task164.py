# ARC Task 164

def solve_6d0aefbc(I):
    # Mirror each row horizontally and keep list - of - lists output
    return [r + r[::-1] for r in I]

p = solve_6d0aefbc
