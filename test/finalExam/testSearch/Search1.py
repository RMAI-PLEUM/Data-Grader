def binary_search(lst, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high)//2
        if target == lst[mid]:
            return True
        elif target < lst[mid]:
            return binary_search(lst, target, low, mid - 1)
        elif target > lst[mid]:
            return binary_search(lst, target, mid+1, high)

def bubble_sort(lst):

    for i in range(len(lst)-1):
        swapped = False
        for j in range(len(lst)-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swapped = True
    return lst


lst, target = input('Enter Input : ').split('/')
lst = list(map(int, lst.split()))
lst = bubble_sort(lst)
target = int(target)
print(binary_search(lst, target, 0, len(lst)))
