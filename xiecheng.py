import gevent
import time
import gevent.monkey
gevent.monkey.patch_all()


def foo(i, a, b, c):
    print('Running in foo' + str(i) + ' ' + str(a) + str(b) + str(c))
    #gevent.sleep(0)
    if i % 10==0:
        return 0
    print('Explicit context switch to foo again')


st = time.clock()
tasks = [gevent.spawn(foo,i, 1, 2,3) for i in range(0,100)]
gevent.joinall(tasks)
print time.clock() - st
"""

st = time.clock()
[foo(i,1,2,3) for i in range(0,100000)]
print time.clock() - st
"""