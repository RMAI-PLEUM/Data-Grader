count = 0
def bouble_sort(lst):
    def swap(i, j):

        lst[i], lst[j] = lst[j], lst[i]


    
    n = len(lst)
    swapped = True
    x = -1
    while swapped:
        swapped = False
        x = x+1
        for i in range(1, n-x):
            if lst[i - 1] > lst[i]:
                swap(i-1, i)
                swapped = True
    return lst

inp = list(map(int,input('Enter Input : ').split()))

