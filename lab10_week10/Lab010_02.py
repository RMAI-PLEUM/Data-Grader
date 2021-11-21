def firstGreaterValue(list, target):
    if len(list) ==  0:
        return None
    list.sort()
    
    if list[0] > target:
        return list[0]
    if list[-1] < target:
        return 'No First Greater Value'
    
    low = 0
    high = len(list)-1
    while low <= high:
        mid = low + (high - low)//2
        if list[mid] <= target:
            low = mid + 1
        else:
            x = list[mid]
            high = mid -1
    return x

lst, targets = input('Enter Input : ').split('/')
lst = list(map(int, lst.split(' ')))
targets = list(map(int, targets.split(' ')))
for i in targets:
    print(firstGreaterValue(lst, i))