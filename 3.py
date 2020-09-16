import functools as ft

a = [0, 1, 2, 3, 4, 5]
assert [x for x in a if not x % 2] == list(filter(lambda x: (x % 2 == 0), a))
