import functools as ft

a = [0, 0, 1, 1, 2, 2]
assert list(set(a)) == ft.reduce(lambda l, x: l.append(x) or l if x not in l else l, a, [])
