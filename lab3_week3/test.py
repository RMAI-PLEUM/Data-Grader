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
        s = ' '
        for ele in self.items:
            s += str(ele)+' '
        return s

str = "backtoschool"
l = list(str)
print(l)
print("".join(l))
s = Stack()
s.push('a')
s.push('b')
print(s)