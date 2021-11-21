def bubbleSort(list):
    result = list.copy()
    for i in range(len(result)-1):
        swapped = False
        for j in range(len(result)-1-i):
            if result[j] > result[j+1]:
                result[j], result[j+1] = result[j+1], result[j]
                swapped = True
        if not swapped:
            break
    return result

def sort_subset(target, lst, left = 0, res=[], carry=[]):
    if left >= len(lst):
        return res
    carry.append(lst[left])
    if sum(carry) == target:
        res.append(carry.copy())
    res = sort_subset(target, lst, left+1, res, carry)
    carry.pop()
    res = sort_subset(target, lst, left+1, res, carry)
    return res

def list_sort(list):
    for i in range(len(list)-1):
        swapped = False
        for j in range(len(list)-i-1):
            if len(list[j]) > len(list[j+1]):
                list[j], list[j+1] = list[j+1], list[j]
                swapped = True
        if not swapped:
            break
    return list

inp = input('Enter Input : ').split('/')
target = int(inp[0])
inlist = list(map(int, inp[1].split()))
inlist = bubbleSort(inlist)
vlist = sort_subset(target, inlist)
if len(vlist) == 0:
    print('No Subset')
else:
    vlist = list_sort(vlist)
    for i in vlist:
        print(i)