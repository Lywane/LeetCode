import random
def bs(list,k,start,end):
    if end == 0:
        return None
    else:
        m = (start+end)/2
        if list[m] == k:
            return m
        elif list[m]<k:
            return bs(list,k,m+1,end)
        elif list[m]>k:
            return bs(list,k,0,m)

def for_bs(list,k,i,j):
    while i <= j:
        m = (i+j)/2
        if list[m]==k:
            return m
        elif list[m]<k:
            i=m+1
        elif list[m]>k:
            j=m-1
    return None


if __name__ == '__main__':
    list = [i for i in xrange(3001,10000)]
    size = len(list)
    print for_bs(list,8841,0,size-1)