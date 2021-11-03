def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

a, b = list(map(int, input('Enter Input : ').split()))
print(gcd(a,b))