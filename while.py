# while
val = 10
while val != 1:
    print(val)
    val -= 1
else:
    print("end")

while 1 > 0:
    print("begin")
    break
else:  # this block will be executed if no Exception and Break and Return in the section before
    pass  # just for syntactically requirement
