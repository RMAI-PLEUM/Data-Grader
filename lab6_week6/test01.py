   
def printNTo1(n):
    if n == 0:
        return 
    print(n, end=' ')
    if n>0 :
        printNTo1(n-1)

def print1ToN(n):

    if n > 1 :
        print1ToN(n - 1)
    print(n, end=' ')
    return

print1ToN(5)    
printNTo1(5)
