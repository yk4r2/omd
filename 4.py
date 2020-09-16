a = ['foo', 'bar', 'baz']

assert dict(enumerate(a)) == {index: x for index, x in enumerate(a)}
