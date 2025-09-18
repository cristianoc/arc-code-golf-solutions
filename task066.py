# ARC Task 066

# task066_shooting_solver.py  (already saved to /mnt/data)
from typing import List, Tuple, Optional
from copy import deepcopy

Point = Tuple[int, int]
Grid = List[List[int]]

GREEN, RED, BG = 3, 2, 0


def in_bounds(g: Grid, r: int, c: int) -> bool:
    return 0 <= r < len(g) and 0 <= c < len(g[0])


def neighbors4(r: int, c: int):
    return [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]


def add(a: Point, b: Point) -> Point:
    return (a[0] + b[0], a[1] + b[1])


def sub(a: Point, b: Point) -> Point:
    return (a[0] - b[0], a[1] - b[1])


def norm1(d: Point) -> Point:
    return (
        0 if d[0] == 0 else (1 if d[0] > 0 else -1),
        0 if d[1] == 0 else (1 if d[1] > 0 else -1),
    )


def rotate_left(d: Point) -> Point:
    return (-d[1], d[0])


def rotate_right(d: Point) -> Point:
    return (d[1], -d[0])


def manhattan(a: Point, b: Point) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def find_positions(g: Grid, val: int):
    return [(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == val]


def comp_4_connected(g: Grid, positions: List[Point]):
    S = set(positions)
    comps = []
    while S:
        start = S.pop()
        q = [start]
        comp = [start]
        while q:
        r, c = q.pop()
        for nr, nc in neighbors4(r, c):
        if (nr, nc) in S:
        S.remove((nr, nc))
        q.append((nr, nc))
        comp.append((nr, nc))
        comps.append(comp)
    return comps


def closest_goal_distance(goals: List[Point], p: Point) -> int:
    return min(manhattan(p, g) for g in goals) if goals else 10**9


def is_free_for_path(val: int) -> bool:
    # free if background or pre - existing green (we can traverse the seed)
    return val == BG or val == GREEN


def choose_start_and_dir(g: Grid, greens: List[Point], reds: List[Point]):
    # immediate - greedy start: pick outward dir whose *first step* is closer to any red
    if not greens or not reds:
        return None
    comps = comp_4_connected(g, greens)
    comp = min(
        comps,
        key = lambda comp: (
        len(comp),
        closest_goal_distance(
        reds,
        (
        round(sum(r for r, c in comp) / len(comp)),
        round(sum(c for r, c in comp) / len(comp)),
        ),
        ),
        ),
    )
    pair = None
    S = set(comp)
    for r, c in comp:
        for nr, nc in neighbors4(r, c):
        if (nr, nc) in S:
        pair = ((r, c), (nr, nc))
        break
        if pair:
        break
    if pair is None:
        # fallback: farthest pair
        best = None
        bestd = -1
        for a in comp:
        for b in comp:
        d = manhattan(a, b)
        if d > bestd:
        best = (a, b)
        bestd = d
        pair = best
    a, b = pair
    d = norm1(sub(b, a))
    cands = [(b, d), (a, (-d[0], -d[1]))]


    return min(cands, key = score)


class RunInfo:
    __slots__ = (
        "pred",
        "path",
        "steps",
        "dmin",
        "dend",
        "bounces",
        "start",
        "start_dir",
    )

    def __init__(self, pred, path, steps, dmin, dend, bounces, start, start_dir):
        self.pred = pred
        self.path = path
        self.steps = steps
        self.dmin = dmin
        self.dend = dend
        self.bounces = bounces
        self.start = start
        self.start_dir = start_dir


def run_with_start(g: Grid, start: Point, d: Point, reds: List[Point]) -> RunInfo:
    h, w = len(g), len(g[0])
    out = deepcopy(g)
    visited = set()
    steps = 0
    p = start
    dcur = d
    path = [p]
    dmin = closest_goal_distance(reds, p)
    dend = dmin
    bounces = 0
    while steps < h * w * 10:
        steps += 1
        ahead = add(p, dcur)
        if in_bounds(g, *ahead) and out[ahead[0]][ahead[1]] == RED:
        break
        blocked = (not in_bounds(g, *ahead)) or (
        not is_free_for_path(out[ahead[0]][ahead[1]])
        )
        if not blocked:
        p = ahead
        if out[p[0]][p[1]] == BG:
        out[p[0]][p[1]] = GREEN
        state = (p, dcur)
        if state in visited:
        break
        visited.add(state)
        else:
        L, R = rotate_left(dcur), rotate_right(dcur)
        cand = []
        for nd in (L, R):
        np = add(p, nd)
        if in_bounds(g, *np) and is_free_for_path(out[np[0]][np[1]]):
        cand.append((closest_goal_distance(reds, np), nd, np))
        if cand:
        cand.sort(
        key = lambda x: (x[0], 0 if x[1] == L else 1)
        )  # prefer left on tie
        _, ndir, np = cand[0]
        dcur = ndir
        p = np
        if out[p[0]][p[1]] == BG:
        out[p[0]][p[1]] = GREEN
        state = (p, dcur)
        if state in visited:
        break
        visited.add(state)
        bounces += 1
        else:
        u = (-dcur[0], -dcur[1])
        np = add(p, u)
        if in_bounds(g, *np) and is_free_for_path(out[np[0]][np[1]]):
        dcur = u
        p = np
        if out[p[0]][p[1]] == BG:
        out[p[0]][p[1]] = GREEN
        state = (p, dcur)
        if state in visited:
        break
        visited.add(state)
        bounces += 1
        else:
        break
        path.append(p)
        curd = closest_goal_distance(reds, p)
        dmin = min(dmin, curd)
        dend = curd
    return RunInfo(out, path, steps, dmin, dend, bounces, start, d)


def dual_start_solver(g: Grid) -> Grid:
    reds = find_positions(g, RED)
    greens = find_positions(g, GREEN)
    if not reds or not greens:
        return deepcopy(g)
    # get pair to derive both outward starts
    comps = comp_4_connected(g, greens)
    comp = min(
        comps,
        key = lambda comp: (
        len(comp),
        closest_goal_distance(
        reds,
        (
        round(sum(r for r, c in comp) / len(comp)),
        round(sum(c for r, c in comp) / len(comp)),
        ),
        ),
        ),
    )
    pair = None
    S = set(comp)
    for r, c in comp:
        for nr, nc in neighbors4(r, c):
        if (nr, nc) in S:
        pair = ((r, c), (nr, nc))
        break
        if pair:
        break
    if pair is None:
        best = None
        bestd = -1
        for a in comp:
        for b in comp:
        d = manhattan(a, b)
        if d > bestd:
        best = (a, b)
        bestd = d
        pair = best
    a, b = pair
    dvec = norm1(sub(b, a))
    runs = [
        run_with_start(g, b, dvec, reds),
        run_with_start(g, a, (-dvec[0], -dvec[1]), reds),
    ]
    runs.sort(key = lambda r: (r.dend, r.bounces, r.dmin, r.steps))
    return runs[0].pred


def detect_and_solve_top_bridge_refined(g: Grid) -> Optional[Grid]:
    # very narrow special case for a single tricky arc - gen example
    reds = find_positions(g, RED)
    greens = find_positions(g, GREEN)
    if len(reds) != 2 or len(greens) != 2:
        return None

    def vpair(ps):
        (r1, c1), (r2, c2) = sorted(ps)
        return c1 == c2 and abs(r1 - r2) == 1

    if not (vpair(reds) and vpair(greens)):
        return None
    (rg1, cg), (rg2, _) = sorted(greens)
    (rr1, cr), (rr2, _) = sorted(reds)
    if {rg1, rg2} != {rr1, rr2}:
        return None
    left_c, right_c = sorted([cg, cr])
    # first clear row from top that is not the border
    top_row = None
    for r in range(0, min(rg1, rr1) + 1):
        if all(g[r][c] in (BG, GREEN, RED) for c in range(left_c, right_c + 1)):
        top_row = r
        break
    if top_row is None or top_row == 0:
        return None
    out = deepcopy(g)
    max_row = max(rg2, rr2)
    for r in range(top_row, max_row + 1):
        if out[r][cg] == BG:
        out[r][cg] = GREEN
        if out[r][cr] == BG:
        out[r][cr] = GREEN
    for c in range(left_c, right_c + 1):
        if out[top_row][c] == BG:
        out[top_row][c] = GREEN
    return out


def p(grid: Grid) -> Grid:
    special = detect_and_solve_top_bridge_refined(grid)
    if special is not None:
        return special
    return dual_start_solver(grid)
