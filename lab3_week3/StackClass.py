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
    
    def __str__(self):
        s = ' '
        for ele in self.items:
            s += str(ele)+' '
        return s
    
    def value(self):
        s = ''
        i = len(self.items)-1
        while i >= 0:
            s += self.items[i]
            i-=1
        return s  


j = ['a','b','c']
e = Stack(j)
print(e.value())

