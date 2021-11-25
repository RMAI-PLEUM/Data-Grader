def binary_search(lst, target, low, high):
    if low > high:
        return False
    else:
        mid = (low+high)//2
        if target == lst[mid]:
            return True
        elif target < lst[mid]:
            return binary_search(lst, target, low, mid-1)
        elif target > lst[mid]:
            return binary_search(lst, target, mid+1, high)


# test
l = [1,2,4,6,7,8,9]
print(binary_search(l,2,0,len(l)))