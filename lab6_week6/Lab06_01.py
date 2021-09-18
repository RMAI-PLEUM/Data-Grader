def print1ToN(n):
    if n == 1 :
        return 1
    else:
        print1ToN(n-1)

# def printNto1(n):
#     #code here

n = int(input("Enter Input : "))

print(print1ToN(n))
# printNto1(n)

# def fiboR(n) :
#   if n == 0 or n == 1 :
#     return n
#   else :
#     return fiboR(n-1) + fiboR(n-2)

# print(fiboR())