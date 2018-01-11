# set
bob = frozenset({'17', 15, "aaa"})
Frank = {'17', 16, "bbb"}
Frank.add(1414)
un = bob.union(Frank)
ints = bob.intersection(Frank)
print("")