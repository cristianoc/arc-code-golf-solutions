# ARC Task 046


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

def identity(x):
    return x

def add(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    elif isinstance(a, tuple) and isinstance(b, tuple):
        return (a[0] + b[0], a[1] + b[1])
    elif isinstance(a, int) and isinstance(b, tuple):
        return (a + b[0], a + b[1])
    elif isinstance(a, tuple) and isinstance(b, int):
        return (a[0] + b, a[1] + b)
    return (a, b)

def subtract(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a - b
    elif isinstance(a, tuple) and isinstance(b, tuple):
        return (a[0] - b[0], a[1] - b[1])
    elif isinstance(a, int) and isinstance(b, tuple):
        return (a - b[0], a - b[1])
    elif isinstance(a, tuple) and isinstance(b, int):
        return (a[0] - b, a[1] - b)
    return (0, 0)










def combine(a, b):
    # Concatenate tuples, union sets; otherwise fall back to tuple concat
    if isinstance(a, tuple) and isinstance(b, tuple):
        return a + b
    if isinstance(a, set) and isinstance(b, set):
        return a | b
    return tuple(a) + tuple(b)

def intersection(a, b):
    return a & b



def order(container, compfunc):
    return tuple(sorted(container, key = compfunc))



def size(container):
    return len(container)







def argmin(container, compfunc):
    return min(container, key = compfunc)



def initset(value):
    return {value}




def decrement(x):
    # Integer - only in this task's usage
    return x - 1






def sfilter(container, condition):
    return type(container)((e for e in container if condition(e)))




def first(container):
    return next(iter(container))

def last(container):
    return max(enumerate(container))[1]


def remove(value, container):
    return type(container)((e for e in container if e != value))

def other(container, value):
    return first(remove(value, container))


def astuple(a, b):
    return (a, b)




def compose(outer, inner):
    return lambda x: outer(inner(x))

def chain(h, g, f):
    return lambda x: h(g(f(x)))

def matcher(function, target):
    return lambda x: function(x) == target

def rbind(function, fixed):
    n = function.__code__.co_argcount
    if n == 2:
        return lambda x: function(x, fixed)
    elif n == 3:
        return lambda x, y: function(x, y, fixed)
    else:
        return lambda x, y, z: function(x, y, z, fixed)

def lbind(function, fixed):
    n = function.__code__.co_argcount
    if n == 2:
        return lambda y: function(fixed, y)
    elif n == 3:
        return lambda y, z: function(fixed, y, z)
    else:
        return lambda y, z, a: function(fixed, y, z, a)

def power(function, n):
    if n == 1:
        return function
    return compose(function, power(function, n - 1))

def fork(outer, a, b):
    return lambda x: outer(a(x), b(x))

def apply(function, container):
    return type(container)((function(e) for e in container))






def mostcolor(element):
    values = [v for r in element for v in r] if isinstance(element, tuple) else [t[0] for t in element]
    return max(set(values), key = values.count)



def width(piece):
    if len(piece) == 0:
        return 0
    if isinstance(piece, tuple):
        return len(piece[0])
    return rightmost(piece) - leftmost(piece) + 1






def asindices(grid):
    return set((i, j) for i in range(len(grid)) for j in range(len(grid[0])))







def toindices(patch):
    if len(patch) == 0:
        return set()
    first_item = next(iter(patch))
    if isinstance(first_item, tuple) and len(first_item) == 2 and isinstance(first_item[1], tuple):
        return set(index for _, index in patch)
    return patch

def recolor(value, patch):
    return set((value, index) for index in toindices(patch))

def shift(patch, directions):
    if len(patch) == 0:
        return patch
    di, dj = directions
    first_item = next(iter(patch))
    if isinstance(first_item, tuple) and len(first_item) == 2 and isinstance(first_item[1], tuple):
        return set((value, (i + di, j + dj)) for value, (i, j) in patch)
    return set((i + di, j + dj) for i, j in patch)


def dneighbors(loc):
    return {
        (loc[0] - 1, loc[1]),
        (loc[0] + 1, loc[1]),
        (loc[0], loc[1] - 1),
        (loc[0], loc[1] + 1),
    }



def objects(grid, univalued, diagonal, without_bg):
    bg = mostcolor(grid) if without_bg else None
    objs = []
    occupied = set()
    h, w = (len(grid), len(grid[0]))
    unvisited = asindices(grid)
    diagfun = neighbors if diagonal else dneighbors
    for loc in unvisited:
        if loc in occupied:
        continue
        val0 = grid[loc[0]][loc[1]]
        if val0 == bg:
        continue
        obj = {(val0, loc)}
        cands = {loc}
        while cands:
        neighborhood = set()
        for cand in cands:
        v = grid[cand[0]][cand[1]]
        if (val0 == v) if univalued else (v != bg):
        obj.add((v, cand))
        occupied.add(cand)
        neighborhood |= {(i, j) for i, j in diagfun(cand) if 0 <= i < h and 0 <= j < w}
        cands = neighborhood - occupied
        objs.append(obj)
    return objs





def leftmost(patch):
    return min((j for i, j in toindices(patch)))

def rightmost(patch):
    return max((j for i, j in toindices(patch)))










def palette(element):
    # Deterministic palette:
    # - For full grids (tuple of rows), keep behavior as a set of colors.
    # - For objects/patches (set of (value, (i, j))), return colors ordered
    #   by descending frequency within the object; break ties by the
    #   leftmost column where the color appears. This stabilizes subsequent
    #   selection of a non - 5 color.
    if isinstance(element, tuple):
        return {v for r in element for v in r}
    # element is a collection of (value, (i, j)) pairs
    counts = {}
    leftmost_col = {}
    for v, (i, j) in element:
        counts[v] = counts.get(v, 0) + 1
        if v not in leftmost_col or j < leftmost_col[v]:
        leftmost_col[v] = j
    colors = list(counts.keys())
    colors.sort(key = lambda c: (-counts[c], leftmost_col.get(c, 1 << 30), c))
    return tuple(colors)













def paint(grid, obj):
    h, w = (len(grid), len(grid[0]))
    grid_painted = list((list(row) for row in grid))
    for value, (i, j) in obj:
        if 0 <= i < h and 0 <= j < w:
        grid_painted[i][j] = value
    return tuple((tuple(row) for row in grid_painted))





def upscale(element, factor):
    if isinstance(element, tuple):
        rows = []
        for row in element:
        expanded = []
        for value in row:
        expanded.extend([value] * factor)
        for _ in range(factor):
        rows.append(tuple(expanded))
        return tuple(rows)
    else:
        if len(element) == 0:
        return set()
        di_inv, dj_inv = ulcorner(element)
        di, dj = (-di_inv, -dj_inv)
        normed_obj = shift(element, (di, dj))
        o = set()
        for value, (i, j) in normed_obj:
        for io in range(factor):
        for jo in range(factor):
        o.add((value, (i * factor + io, j * factor + jo)))
        return shift(o, (di_inv, dj_inv))













def canvas(value, dimensions):
    return tuple((tuple((value for j in range(dimensions[1]))) for i in range(dimensions[0])))














def gravitate(source, destination):
    si, sj = center(source)
    di, dj = center(destination)
    i, j = (0, 0)
    if vmatching(source, destination):
        i = 1 if si < di else -1
    else:
        j = 1 if sj < dj else -1
    gi, gj = (i, j)
    c = 0
    while not adjacent(source, destination) and c < 42:
        c += 1
        gi += i
        gj += j
        source = shift(source, (i, j))
    return (gi - i, gj - j)










def solve_234bbc79(I):
    # Normalize input to immutable tuples so helpers treat it as a grid
    if not isinstance(I, tuple):
        I = tuple(tuple(row) for row in I)
    x1 = objects(I, F, F, T)
    x2 = rbind(other, FIVE)
    x3 = compose(x2, palette)
    x4 = fork(recolor, x3, identity)
    x5 = apply(x4, x1)
    x6 = order(x5, leftmost)
    x7 = compose(last, last)
    x8 = lbind(matcher, x7)
    x9 = compose(x8, leftmost)
    x10 = compose(x8, rightmost)
    x11 = fork(sfilter, identity, x9)
    x12 = fork(sfilter, identity, x10)
    x13 = compose(dneighbors, last)
    x14 = rbind(chain, x13)
    x15 = lbind(x14, size)
    x16 = lbind(rbind, intersection)
    x17 = chain(x15, x16, toindices)
    x18 = fork(argmin, x11, x17)
    x19 = fork(argmin, x12, x17)
    x20 = compose(last, x18)
    x21 = compose(last, x19)
    x22 = astuple(ZERO, DOWN_LEFT)
    x23 = initset(x22)
    x24 = lbind(add, RIGHT)
    x25 = chain(x20, first, last)
    x26 = compose(x21, first)
    x27 = fork(subtract, x26, x25)
    x28 = compose(first, last)
    x29 = compose(x24, x27)
    x30 = fork(shift, x28, x29)
    x31 = fork(combine, first, x30)
    x32 = fork(remove, x28, last)
    x33 = fork(astuple, x31, x32)
    x34 = size(x1)
    x35 = power(x33, x34)
    x36 = astuple(x23, x6)
    x37 = x35(x36)
    x38 = first(x37)
    x39 = width(x38)
    x40 = decrement(x39)
    x41 = astuple(THREE, x40)
    x42 = canvas(ZERO, x41)
    O = paint(x42, x38)
    return [list(row) for row in O]

def p(g):
    return solve_234bbc79(g)
