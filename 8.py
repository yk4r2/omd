a = {0:'foo',1:'bar',2:'baz'}

assert dict(reversed(list(a.items()))) == {k: v for k, v in reversed(a.items())}
