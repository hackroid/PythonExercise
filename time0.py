# time
import time

ticks = time.time()
print(ticks)
localtime = time.localtime(ticks)
print(localtime, localtime[0])  # tuple
asctime = time.asctime(localtime)
print(asctime, asctime[1])  # str
altzone = time.altzone
print(altzone)
ctime = time.ctime(ticks)  # str
print(ctime)
gmtime = time.gmtime(ticks)  # tuple
print(gmtime)
mktime = time.mktime(gmtime)
print(mktime)
t1 = time.clock()
time.sleep(1)
t2 = time.clock()
print(t2 - t1)
timezone = time.timezone
print(timezone)
tzname = time.tzname
print(tzname)