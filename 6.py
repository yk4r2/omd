a = ['foo','bar','baz','egg']
b = ['bar', 'baz']

print('Отсутствуют:')
[print(i) for i in list(set(a) - set(b))]

# [print(i) for i in a if i not in set(b)]
