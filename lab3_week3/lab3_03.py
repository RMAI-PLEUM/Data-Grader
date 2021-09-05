class Stack:
    def __init__(self,list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
    
    def push(self,i):
        self.items.append(i)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
    
    
inp = input('Enter Input : ').split()

S = Stack()


i=0
sum = 0
while i<int(len(inp)-1): 
    if (inp[i]==inp[i+1]==inp[i+2]):
        inp.pop(i)
        inp.pop(i)
        inp.pop(i)
        sum+=1
        i=0
    i+=1

S = Stack(list(inp))

if len(inp)==0:
    print(len(inp))
    print("Empty")
else:
    print(S.size())
    e=S.items[::-1]
    for x in e:
        print(x,end="")
    
if sum > 1 :
    print("\nCombo : {} ! ! !".format(sum))



