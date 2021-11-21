def minimumBox(lst, numBox):
    left = max(lst)
    right = sum(lst)
    while left <= right:
        size = (left+right)//2
        count = 0
        i = 0
        while i < len(lst):
            weight = 0
            while i < len(lst) and weight + lst[i] <= size:
                weight += lst[i]
                i += 1
            count += 1

        if count <= numBox:
            right = size-1
        else:
            left = size+1
    return left

lst, numbox = input('Enter Input : ').split('/')
numbox = int(numbox)
lst = list(map(int, lst.split()))
print(f"Minimum weigth for {numbox} box(es) = {minimumBox(lst, numbox)}")