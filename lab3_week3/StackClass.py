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
        return self.items == None

    def size(self):
        return len(self.items)