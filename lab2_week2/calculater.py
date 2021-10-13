class Calculator :

    def __init__(self,x):
        self.x = x

    def __add__(self,other):
        
        return self.x + other.x
    
    def __sub__(self,other):

       return self.x - other.x

    def __mul__(self,other):
        return self.x * other.x

    def __truediv__(self,other):
       return self.x / other.x

x,y = input("Enter num1 num2 : ").split(",")

x,y = Calculator(int(x)),Calculator(int(y))

print(x+y,x-y,x*y,x/y,sep="\n")


