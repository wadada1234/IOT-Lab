#( C) Print current time for 10 times to the current time.
import datetime
x= datetime.datetime.now()
y =x+datetime.timedelta(0,10)
print(x.time())
print(y.time())