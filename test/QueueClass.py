
class Queue:
    def __init__(self, list = None):
        if list is None:
            self.item = []
        else:
            self.item = list
    
    def __str__(self):
        s = ''
        for x in self.item:
            s += str(x) + ' '
        return s

    def enQueue(self, data):
        return self.item.append(data)

    def deQueue(self):
        return self.item.pop(0)

    def isEmpty(self):
        return len(self.item) == 0
    
    def size(self):
        return len(self.item)

# sum = ['a','l','l','m']
# Q = Queue(sum)
# Q.enQueue('!')
# print(Q)
# Q.deQueue()
# print(Q)
# print(Q.isEmpty())
# print(Q.size())

