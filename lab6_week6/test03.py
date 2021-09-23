# def gcd(a,b):
#     if(b==0):
#         return a
#     else:
#         return gcd(b,a%b)
# a,b = input("Enter Input : ").split()
# a = int(a)
# b = int(b)
# if a == 0 and b == 0:
#     print("Error! must be not all zero.")
# else:
#     print("The gcd of {} and {} is : {}".format(a,b,gcd(a,b)))
 
 
def GCD(a, b):
    if a == 0 :
        return b
    return GCD(b%a, a)

a, b = input('Enter Input : ').split()
if int(a.replace('-', '')) < int(b.replace('-', '')) and int(a) != 0:
    c = int(a)
    a = int(b)
    b = c
o = GCD(int(a), int(b))
if o < 0:
    o *= -1
print('The gcd of {} and {} is : {}'.format(a, b, o)) if o != 0 else print('Error! must be not all zero.')