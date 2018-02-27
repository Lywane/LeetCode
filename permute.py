def permute(list):
    sub=[]
    sum=[]
    dfs(list,sub,sum)
    return sum

def dfs(nums,sublist,sum):
    if len(sublist)==len(nums):
        sum.append(sublist[:])
    for i in nums:
        if i in sublist:
            continue
        sublist.append(i)
        dfs(nums,sublist,sum)
        sublist.remove(i)

if __name__ == '__main__':
    print permute([1,2,3])