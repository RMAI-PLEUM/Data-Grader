count = 0
def bubble_sort(lst):
    global count
    def swap(i, j):
        lst[i], lst[j] = lst[j], lst[i]

    n = len(lst)
    swapped = True
    x = -1

    while swapped:
        swapped = False
        x = x+1
        for i in range(1, n-x):
            count += 1
            if lst[i - 1] > lst[i]:
                swap(i-1, i)
                swapped = True
    return lst

print(" *** Bubble sort ***")    
input_string = input("Enter some numbers : ")
A=[]
for n in input_string.split():
	A.append(int(n))
bubble_sort(A)
print()
print(A)
print("Data comparison =", count)
