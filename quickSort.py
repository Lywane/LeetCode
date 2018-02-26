


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


if __name__ == '__main__':
    a = [2,3,34,45,5,2,31,54,31,10,62,21]
    quick(a,0,4)
    print a