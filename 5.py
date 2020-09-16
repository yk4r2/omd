a = [
'John', 'Allison', 'Brian',
'Claire', 'Andrew'
]

for i in range(len(a)):
    if i % 4:
        print(f'Hi {a[i]}!')
    elif i % 4 == 1:
        print('Hi {}!'.format(a[i]))
    elif i % 4 == 2:
        print('Hi %s!' % a[i])
    else:
        print('Hi ' + a[i] + '!')
