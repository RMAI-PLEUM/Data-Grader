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

manga, p = input("Enter Input : ").split('/')
manga = list(manga.split(' '))
p = list(p.split(','))
# print(manga)
# print(p)
titan = Queuelist(manga)
i = 0
duplicate = 0
for i in range(len(p)):
    if 'E' in p[i]:
        p[i] = p[i].strip('E')
        p[i] = p[i].strip(' ')
        titan.enQueue(p[i])

    if 'D' in p[i]:
        titan.deQueue()
check = []
# print(titan.size())
for i in range(titan.size()):
     c = titan.items[i]
     sum = 0
     sum = titan.items.count(c)
     if sum == 2:
         duplicate = 1
     check.append(sum)

# print(titan.value())
if duplicate == 0 :
 print("NO Duplicate")
else:
 print("Duplicate")