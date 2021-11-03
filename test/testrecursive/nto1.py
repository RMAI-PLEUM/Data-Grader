def nto1(n):
    if n == 1:
        print(n)
        return
    else:
        print(n, end=' ')
        nto1(n-1)

def OnetoN(n):
    if n == 1:
        print(n, end=' ')
        return
    if n > 1:
        OnetoN(n-1)
    print(n, end=' ')

inp = int(input('Enter Input : '))
nto1(inp)
OnetoN(inp)