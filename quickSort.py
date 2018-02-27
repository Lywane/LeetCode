


def quick(list,start,end):
    if start < end:
        i, j = start, end
        k = list[i]
        while i < j:
            while (i < j) and (list[j]>=k):
                j-=1
            list[i] = list[j]
            while (i < j) and (list[i]<=k):
                i+=1
            list[j] = list[i]

        list[i]=k
        quick(list,start,i-1)
        quick(list, j+1, end)
    return list

def quick2(list,start,end):
    if start<end:
        i, j = start, end
        k = list[i]
        while i < j :
            while (i<j) and (list[j]>k):
                j-=1
            while (i<j) and (list[i]<k):
                i+=1
            list[i],list[j]=list[j],list[i]
        list[start],list[j]=list[j],list[start]
        quick(list, start, i - 1)
        quick(list, j + 1, end)
    return list


def build_heap(list,size):
    for i in range(0,(size / 2))[::-1]:
        ajust_heap(list,i,size)

def ajust_heap(list,i,size):
    l = 2*i+1
    r = 2*i+2
    m = i
    if i < size/2:
        if l<size and list[l]>list[m]:
            m = l
        if r<size and list[r]>list[m]:
            m = r
        if m!=i:
            list[m],list[i]=list[i],list[m]
            ajust_heap(list,m,size)



def heap_sort(list):
    size = len(list)
    build_heap(list,size)
    for i in range(0,size)[::-1]:
        list[0],list[i] = list[i],list[0]
        ajust_heap(list,0,i)




if __name__ == '__main__':
    a = [2,3,34,45,5,2,31,54,31,10,62,21]
    #quick(a,0,4)
    heap_sort(a)
    print a