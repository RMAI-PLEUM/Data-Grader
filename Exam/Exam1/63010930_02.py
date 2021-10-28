print(" *** Perfect Number Verification ***")
x = int(input("Enter number : "))
if x < 0:
    print("Only positive number !!!")
    exit()
else:
    pagob = []
    i = 1
    while i <= x:
        if (x%i == 0):
            pagob.append(i)
        i+=1
i = 0
sum = 0
for i in pagob:
    sum += i

sum = sum - x

if sum == x:
    print("{} is a PERFECT NUMBER.".format(x))
    print("Factors : {}".format(pagob[0:len(pagob)-1]))
else:
    print("{} is NOT a perfect number.".format(x))
    print("Factors : {}".format(pagob[0:len(pagob)-1]))
