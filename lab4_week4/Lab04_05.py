class Queue:

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
    
    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
    
    def __str__(self):
        if self.isEmpty():
            return 'ytpmE'
        s = ''
        for ele in self.items:
            s += str(ele)
        return s   
    
    def value(self):
        s = ''
        i = len(self.items)-1
        while i >= 0:
            s += self.items[i]
            i-=1
        return s  
data = input('Enter Input (Normal, Mirror) : ').split()
mirrStack = Stack(list(data[1]))
normalStack = Stack()
mirrQ = Queue()
saveMirrStack = Stack()

normalExplose = 0
mirrExplose = 0

while mirrStack.size() > 2:
    e1 = mirrStack.pop()
    e2 = mirrStack.pop()
    e3 = mirrStack.pop()

    if e1 == e2 and e1 == e3:
        mirrQ.enQueue(e1)
        mirrExplose += 1
        
        while saveMirrStack.size() > 0:
            mirrStack.push(saveMirrStack.pop())
    else: 
        saveMirrStack.push(e1)
        mirrStack.push(e3)
        mirrStack.push(e2)

while saveMirrStack.size() > 0:
    mirrStack.push(saveMirrStack.pop())

Fail = 0
for i in data[0]:
    if normalStack.size() < 2:
        normalStack.push(i)
    else:
        e1 = normalStack.pop()
        e2 = normalStack.pop()

        if i != e1 or i != e2:
            normalStack.push(e2)
            normalStack.push(e1)
            normalStack.push(i)
        else:
            if mirrQ.isEmpty() == False:
                e3 = mirrQ.deQueue()
                if e3 == i:
                    Fail += 1
                    normalStack.push(e2)
                else:
                    normalStack.push(e2)
                    normalStack.push(e2)
                    normalStack.push(e3)
                    normalStack.push(i)
            else: normalExplose += 1

print('NORMAL :')
print(normalStack.size())

if normalStack.isEmpty():print("Empty")
else:print(normalStack.value())
print(normalExplose,"Explosive(s) ! ! ! (NORMAL)")

if Fail != 0:
    print("Failed Interrupted {} Bomb(s)".format(Fail))

print('------------MIRROR------------')
print(': RORRIM')
print(mirrStack.size())
print(mirrStack)
print('(RORRIM) ! ! ! (s)evisolpxE {}'.format(mirrExplose))
