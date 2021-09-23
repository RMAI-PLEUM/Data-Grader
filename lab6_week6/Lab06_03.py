def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
a,b = input("Enter Input : ").split()
ans = gcd(int(a), int(b))
if ans < 0:
    ans *= -1
a = int(a)
b = int(b)
if a == 0 and b == 0:
    print('Error! must be not all zero.')
    
if a > 0 and b > 0:
    if a > b:
        print('The gcd of {} and {} is : {}'.format(a, b, ans))
    if a < b:
        print('The gcd of {} and {} is : {}'.format(b, a, ans))
elif a < 0 and b < 0:
    if a < b:
        print('The gcd of {} and {} is : {}'.format(a, b, ans))
    if a > b:
        print('The gcd of {} and {} is : {}'.format(b, a, ans))
elif a > b:
       print('The gcd of {} and {} is : {}'.format(a, b, ans))
elif a < b:
    print('The gcd of {} and {} is : {}'.format(b, a, ans))



