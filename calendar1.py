import calendar
import time

t1 = time.clock()
cal = calendar.month(2018, 1)
print(cal)
t2 = time.clock()
print(t2 - t1)

t1 = time.clock()
a = [1, 4, 32, 4, 76, 45, 3, 76]
print(sorted(a))
t2 = time.clock()
print(t2 - t1)

calen = calendar.calendar(2108, w=0, l=0, c=5)
print(calen)
