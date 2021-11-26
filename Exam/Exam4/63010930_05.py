def binarySearch(arr, left, right, x):
    if left > right:
        return -1
    else:
        mid = (left+right)//2
        if x == arr[mid]:
            return mid
        elif x < arr[mid]:
            
            
            if x > arr[left]:
                print(f'checking left side ({arr[left]}-{arr[mid-1]})')
            if x < arr[4]:
                print(f'checking left side ({arr[3]}-{arr[2]})')



            return binarySearch(arr, left, mid -1, x)

        elif x >= arr[mid]:

            if x <= arr[right]:
                print(f'checking right side ({arr[mid+1]}-{arr[right]})')

            return binarySearch(arr, mid +1, right, x)

print('--Binary Search--')
inp1 = input("Enter input list/search number : ").split("/")
inp = [int(e) for e in inp1[0].split()]
inp.sort()
print("sort with built-in function : "+str(inp))
x = int(inp1[1]) # find this one
 
result = binarySearch(inp, 0, len(inp)-1, x)
 
if result != -1:
    print(str(x)+" is present at index " + str(result))
else:
    print("Not found")