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

q = Queue()
inp = input("Enter Input : ").split(',')
for i in inp:
    if 'E' in i:
        q.enQueue(int(i[2:]))
        print(q.size())
    elif 'D' in i:
        if q.size() == 0:
            print(-1)
        else: 
            print(f'{q.deQueue()} {0}')
        

if q.size() != 0:
    print(q)
else: 
    print('Empty')
