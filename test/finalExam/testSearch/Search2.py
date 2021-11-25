
def firstGreater(lst, num):
    lst.sort()
    if lst[0] > num:
        return lst[0]
    
    # low = 0
    # high = len(lst)-1
    # while low >= high:
    #     mid = (low+high)//2
    #     if num >= lst[mid]:
    #         low = mid + 1
    #     else:
    #         x = lst[mid]
    #         high = mid -1
    # return x
    low = 0
    high = len(lst)-1
    while low <= high:
        mid = low + (high - low)//2
        if lst[mid] <= target:
            low = mid + 1
        else:
            x = lst[mid]
            high = mid -1
    return x

inp = input('Enter Input : ').split('/')
lst = list(map(int, inp[0].split()))
target = int(inp[1])
print(firstGreater(lst, target))