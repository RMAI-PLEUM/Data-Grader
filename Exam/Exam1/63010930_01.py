L = []
i = 0
print(" *** Multiples of 3 or 5 or 7 ***")
x = int(input("Enter number : "))
if x < 0:
    print("Only positive number !!!")
    exit()

while i < x:
    
    if i%3 == 0 or i%5 == 0 or i%7 ==0:
        L.append(i)
    i+=1

Result = 0
for i in L:
    Result += i
print("Result :",Result)
