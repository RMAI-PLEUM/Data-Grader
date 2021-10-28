x = int(input("Enter a positive number : "))
num = {1:"1",2:"2",3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
if x < 1:
    print("{} is too low.".format(x))
if x > 15:
    print("{} is too high.".format(x))
else:
        for i in range(1,x+1):
         print(num[i], end=' ')
        for i in range(x-2):
            for i in range(1,x-2):
                print(num[i+1], end=' ')
                for i in range(x-2):
                    print(' ', end=' ')
                print(num[i])   