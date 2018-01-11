# list
a = [1, 2, 3, 4, 5, 6]
for i in a:
    print(i)
print("a[0]:", a[0])
a.pop()
a.pop(1)
print("a now is:", a)
a.append(7)
print("a now is:", a)
a.insert(1, "-")
print("a now is:", a)
a[1] = '+'
print("a now is:", a)
print(a[0:5:2])
print("len of a is:", len(a))
if a[:2] == a[0:2] and a[3:] == a[3:len(a)]:
    print("true")
if 1 in a:
    print("true")
list2tup = tuple(a)
print(list2tup)
a.clear()
print("a now is:", a)

