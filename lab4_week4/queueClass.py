from collections import deque

class Queuelist:

    def __init__(self, Q = None):
        if Q == None:
            self.items = []
        else:
            self.items = Q
    
    def enQueue(self,i):
        self.items.append(i)

    def deQueue(self):
        return self.items.pop(0)

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
 
    def value(self):
        ch = ''
        i = 0
        for i in range(len(self.items)):
            ch += str(self.items[i])+' ' 
        return ch
    


class Queuedeque:

    def __init__(self,Q = None):
        if Q == None:
            self.items = deque()
        else:
            self.items = deque(Q,len(Q))

    def enQueue(self,i):
        self.items.append(i)

    def deQueue(self):
        return self.items.pop(0)
    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
    
    def value(self):
        ch = ''
        i = 0
        for i in range(len(self.items)):
            ch += str(self.items[i])+' ' 
        return ch


l = [2,3,4,5,6]
q = Queuedeque(l)
q.deQueue()
print(q.value())
