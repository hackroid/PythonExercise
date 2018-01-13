for i in range(1, 7, 2):  # range(start_index_inclusive, end_index_exclusive, step)
    print(i)

students = ('123', 'asd', 'asfda')
for student in students:
    print('student is %s:' % student)
for index, student in enumerate(students):
    print(index, student)

que = ('name', 'color', 'age')
ans = ('Frank', 'green', '16')
for part in zip(que, ans):
    print('what\'s your %s? It\'s %s.' % part)
