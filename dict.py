info = {'name': 'Frank', 'age': '16', 'color': 'green'}
for spec, value in info.items():
    print('%s:' % spec, value)
print()
print(info)
print(*info)


# print(**info)

def intro(**info):
    print('My name is %s, ' % info['name'], end='')
    print('I\'m %s year old, ' % info['age'], end='')
    print('and I love %s' % info['color'])


intro(**info)
