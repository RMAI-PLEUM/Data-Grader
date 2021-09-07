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


data = input("Enter Input : ").split(',')
i = 0
q = Queuelist()
for i in range(len(data)):
    if 'E' in data[i]:
       data[i] =  data[i].strip('E')
       data[i] =  data[i].strip(" ")
       q.enQueue(data[i])
       print(q.size())
    # print(type(data[i]))
    if 'D' in data[i]:
        if (q.size() == 0):
            print("-1")
        else: 
            print("{} {}".format(q.items[0],0))
            q.deQueue()
            
if (q.size()==0):
    print("Empty")        
else:
    print(q.value())
