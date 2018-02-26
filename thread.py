import time
import threadpool
def sayhello(str,port,ip):
    print "Hello {0},port {1},ip {2}".format(str,port,ip)
    time.sleep(2)

name_list =[{'xiaozi':'aa'},{'bb':'cc'}]
start_time = time.time()
pool = threadpool.ThreadPool(10)
requests = threadpool.makeRequests(sayhello, args_list=(name_list,66,"1.1.1.1"))
[pool.putRequest(req) for req in requests]
pool.wait()
print '%d second'% (time.time()-start_time)