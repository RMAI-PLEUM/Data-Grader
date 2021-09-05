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

    def value(self):
        s = ''
        for ele in self.items:
            s += str(ele)+' '
        return s


s = Stack()
data = input("Enter Input : ").split(',')
i = 0
while i<len(data):
    if 'A' in data[i]:
        data[i] = data[i].strip('A')
        data[i] = data[i].strip(' ')
        s.push(int(data[i]))
        print("Add = {} and Size = {}".format(int(data[i]),s.size()))
    if 'P' in data[i]:
        if s.size() == 0:
            print("-1")
        else:
            print("Pop = {} and Index = {}".format(s.pop(),s.size()))
    i = i+1

print("Value in Stack = ",end="")
if s.size() == 0:
    print("Empty")
else:
    print(s.value())

 
   


