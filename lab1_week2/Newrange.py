def NewRange(*args):
    Range = []
    i = 0
    if len(args) == 1:
        
        while(i < args[0]):
            Range.append(float(i))
            i+=1
        return tuple(Range)

    elif(len(args)==2):
        i = args[0]//1
        sum = args[0]
        while(i < args[1]):
            Range.append(sum)
            sum+=1
            i+=1
        return tuple(Range)

    elif(len(args)==3):
        i = args[0]
        j = args[1]
        while(i < j):
            i = float(str(i)[:-1].rstrip('0')) if str(i)[-2] == '0' and str(i)[-3] == '0' else i
            Range.append(i)
            i+=args[2]
        return tuple(Range)

    
print("*** New Range ***")
num = input("Enter Input : ").split(" ")

if len(num)==1:
    print(NewRange(float(num[0])))
elif len(num)==2:
    num1,num2 = list(map(float,num))
    print(NewRange(num1,num2))
elif len(num)==3:
    num1,num2,num3 = list(map(float,num))
    print(NewRange(num1,num2,num3))
    