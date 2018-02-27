#coding=utf8
# 根据列表构造完全二叉树
# 最后一个非叶节点的索引是列表长度除以2后再减去1
# 判断这个非叶节点的值和他的叶子节点大小，需要注意他可能有一个叶子节点，也可能有两个
# 先比较左叶子节点和非叶节点的值，如果左叶比非叶子大，就交换位置。
# 再比较右边。比较时保证列表别越界
# 一直比较到根节点为止
#



def adjust_heap(lists, i, size):
    lchild = 2 * i + 1
    rchild = 2 * i + 2
    max = i
    if i < size / 2:
        if lchild < size and lists[lchild] > lists[max]:
            max = lchild
        if rchild < size and lists[rchild] > lists[max]:
            max = rchild
        if max != i:
            lists[max], lists[i] = lists[i], lists[max]
            adjust_heap(lists, max, size)


def build_heap(lists, size):
    print range(0, (size / 2))[::-1]
    # 从列表长度的一半往前倒
    for i in range(0, (size / 2))[::-1]:
        #调整堆
        adjust_heap(lists, i, size)


def heap_sort(lists):
    #列表大小
    size = len(lists)
    #建造大顶堆
    build_heap(lists, size)
    for i in range(0, size)[::-1]:
        #堆顶和最后元素互换
        lists[0], lists[i] = lists[i], lists[0]
        #调整除去最后一个元素的剩余部分
        adjust_heap(lists, 0, i)

if __name__ == '__main__':
    tmp = [16,7,3,20,17,8]
    heap_sort(tmp)
    print tmp



