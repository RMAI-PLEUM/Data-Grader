def bubble_sort(x,count = 0):
    ans = x.copy()
    for i in range(len(ans)-1):
        change = False
        for j in range(len(ans)-1-i):
            count += 1
            if ans[j] > ans[j+1]:
                ans[j], ans[j+1] = ans[j+1], ans[j]
                change = True
        if not change:
            break
    return '{}\nData comparison = {}'.format(ans,count)

print(" *** Bubble sort ***")    
input_string = input("Enter some numbers : ")
A=[]
for n in input_string.split():
    A.append(int(n))
print(bubble_sort(A))