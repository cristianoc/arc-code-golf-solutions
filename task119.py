# ARC Task 119


F = False
T = True

ZERO = 0
ONE = 1
TWO = 2
THREE = 3
FOUR = 4
FIVE = 5
SIX = 6
SEVEN = 7
EIGHT = 8
NINE = 9
TEN = 10

NEG_ONE = -1
NEG_TWO = -2

DOWN = (1, 0)
RIGHT = (0, 1)
UP = (-1, 0)
LEFT = (0, -1)

ORIGIN = (0, 0)
UNITY = (1, 1)
NEG_UNITY = (-1, -1)
UP_RIGHT = (-1, 1)
DOWN_LEFT = (1, -1)

ZERO_BY_TWO = (0, 2)
TWO_BY_ZERO = (2, 0)
TWO_BY_TWO = (2, 2)
THREE_BY_THREE = (3, 3)

























































# Removed unused rbind/lbind helpers


































































# Removed unused upscale helper



























# Removed unused gravitate helper










def solve_508bd3b6(I):
    # Geometry - based V - shape construction inferred from data
    h, w = len(I), len(I[0])
    grid = [list(row) for row in I]

    twos = [(i, j) for i in range(h) for j in range(w) if I[i][j] == 2]
    eights = [(i, j) for i in range(h) for j in range(w) if I[i][j] == 8]
    if not eights or not twos:
        return grid

    rows2 = {i for i, _ in twos}
    cols2 = {j for _, j in twos}
    is_vertical_bar = len(rows2) == h and len(cols2) >= 1
    is_horizontal_bar = len(cols2) == w and len(rows2) >= 1

    # Determine dominant diagonal among 8s via majority on (j - i) vs (i + j)
    from collections import Counter
    diffs = Counter(j - i for i, j in eights)
    sums = Counter(i + j for i, j in eights)
    diff_k, diff_cnt = (None, 0)
    if diffs:
        diff_k, diff_cnt = diffs.most_common(1)[0]
    sum_k, sum_cnt = (None, 0)
    if sums:
        sum_k, sum_cnt = sums.most_common(1)[0]
    if diff_cnt >= sum_cnt and diff_cnt > 0:
        slope = 1
        k = diff_k
    else:
        slope = -1
        k = sum_k

    # Extension direction: toward the 2 - block
    if is_horizontal_bar:
        # Determine if the horizontal bar is at the bottom or top
        bar_top = min(rows2) == 0
        # Try both directions along same slope; choose the one that paints more zeros
        def simulate(di):
        dj = di if slope == 1 else -di
        start_i, start_j = min(eights)
        cnt = 0
        last = None
        i, j = start_i + di, start_j + dj
        while 0 <= i < h and 0 <= j < w:
        if (i, j) in twos_set:
        break
        if grid[i][j] == 0:
        cnt += 1
        last = (i, j)
        i += di
        j += dj
        return cnt, last
        # Prepare twos_set for simulate
        twos_set = set(twos)
        cnt_down, _ = simulate(1 if bar_top else -1)
        cnt_up, _ = simulate(-1 if bar_top else 1)
        di = (1 if bar_top else -1) if cnt_down >= cnt_up else (-1 if bar_top else 1)
        dj = di if slope == 1 else -di
    else:
        # vertical bar on left or right — move along same slope towards that side
        bar_right = min(cols2) > sum(j for _, j in eights) / len(eights)
        if slope == 1:
        di = 1 if bar_right else -1
        dj = di
        else:
        di = -1 if bar_right else 1
        dj = -di

    start_i, start_j = min(eights)
    twos_set = set(twos)

    last_painted = None
    i, j = start_i + di, start_j + dj
    while 0 <= i < h and 0 <= j < w:
        if (i, j) in twos_set:
        break
        if grid[i][j] == 0:
        grid[i][j] = 3
        last_painted = (i, j)
        i += di
        j += dj

    if last_painted is None:
        i, j = start_i + di, start_j + dj
        prev = None
        while 0 <= i < h and 0 <= j < w and (i, j) not in twos_set:
        prev = (i, j)
        i += di
        j += dj
        last_painted = prev

    if last_painted is None:
        return I

    # From last painted point, draw opposite - slope diagonal moving away from the 2 - block.
    pi, pj = last_painted
    if is_horizontal_bar:
        # Move away from the bar: upward if bar at bottom, downward if bar at top
        bar_top = min(rows2) == 0
        di2 = 1 if bar_top else -1
        # Opposite slope: if original slope +1, opposite is -1 (dj2 = -di2); if original -1, opposite is +1 (dj2 = di2)
        dj2 = -di2 if slope == 1 else di2
    else:
        # Vertical bar: move horizontally away from the bar (left if bar on right, right if bar on left)
        bar_right = min(cols2) > sum(j for _, j in eights) / len(eights)
        dj_target = -1 if bar_right else 1
        # Two possible directions along opposite slope
        up_di2 = -1
        up_dj2 = dj_target
        down_di2 = 1
        down_dj2 = dj_target
        # Prefer the direction whose first step paints a new zero (and is not in 2 - block)
        def can_paint(di2_, dj2_):
        ii, jj = pi + di2_, pj + dj2_
        return 0 <= ii < h and 0 <= jj < w and (ii, jj) not in twos_set and grid[ii][jj] == 0
        if can_paint(up_di2, up_dj2):
        di2, dj2 = up_di2, up_dj2
        else:
        di2, dj2 = down_di2, down_dj2
        i, j = pi + di2, pj + dj2
        while 0 <= i < h and 0 <= j < w:
        if (i, j) in twos_set:
        break
        if grid[i][j] == 0:
        grid[i][j] = 3
        i += di2
        j += dj2
        return grid
    # Horizontal bar opposite - slope upwards drawing
    i, j = pi + di2, pj + dj2
    while 0 <= i < h and 0 <= j < w:
        if (i, j) in twos_set:
        break
        if grid[i][j] == 0:
        grid[i][j] = 3
        i += di2
        j += dj2
    return grid

def p(g):
    return solve_508bd3b6(g)
