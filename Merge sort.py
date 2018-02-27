#coding=utf8
import time
import random
def my_merge(list):
    l = []
    r = []
    result = []
    size = len(list)
    if size < 2:
        return list
    else:
        for i in xrange(1,len(list)):
            if list[i] >= list[0]:
                r.append(list[i])
            if list[i] < list[0]:
                l.append(list[i])
        result.extend(my_merge(l))
        result.append(list[0])
        result.extend(my_merge(r))
        return result


def merge(left, right):
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


def merge_sort(lists):
    # 归并排序
    if len(lists) <= 1:
        return lists
    num = len(lists) / 2
    left = merge_sort(lists[:num])
    right = merge_sort(lists[num:])
    return merge(left, right)


if __name__ == '__main__':
    list = []
    for i in xrange(0,1000):
        list.append(random.choice(range(100000)))
    st =time.time()
    print my_merge(list)

    print time.time()-st
    print merge_sort(list)
    print time.time() - st