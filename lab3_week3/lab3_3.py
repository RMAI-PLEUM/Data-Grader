class Stack :
    
    def __init__(self, list = None):
        if(list == None):
            self.items = []
        else:
            self.items = list

    def push(self,i):
        self.items.append(i)

    def pop(self):
        self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

inp = input('Enter Input : ').split()
combo = 0
s = Stack(list(inp))
backs = Stack()

while s.size() >2:
    a=s.items.pop()
    b=s.items.pop()
    c=s.items.pop()
    
    if a==b and a==c:
        combo +=1
        
        for i in range(backs.size()) :
            s.push(backs.items.pop())             
    else:
        s.push(c)
        s.push(b)
        backs.push(a)
        
while backs.size() > 0:
    s.push(backs.items.pop())

if(combo >1 and s.size()>0):
    print(s.size())
    e=s.items[::-1]
    for x in e:
        print(x,end="")
    print()
    print("Combo : {} ! ! !".format(str(combo)))

if combo > 1 and s.size()==0:
    print(s.size())
    print("Empty")
    print("Combo : {} ! ! !".format(str(combo)))


if combo <= 1 and s.size()==0:
    print(s.size())
    print("Empty")

if combo <=1 and s.size() >0:
    print(s.size())
    e=s.items[::-1]
    for x in e:
        print(x,end="")


        