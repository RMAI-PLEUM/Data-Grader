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
 
    def __str__(self):
        ch = ''
        i = 0
        for i in range(len(self.items)):
            ch += str(self.items[i])+' ' 
        return ch


data = input("Enter people and time : ").split()
main = [i for i in data[0]]

people = Queuelist(main)
cash1 = Queuelist()
cash2 = Queuelist()
check = 0
count1 = 0
count2 = 0

for i in range(1,int(data[1])+1):
    item = ""
    if not people.isEmpty(): 
        item += people.deQueue()
    else: check += 1

    if i > 2:
        if count1 == 3: 
            cash1.deQueue()
            count1 = 0
        if count2 == 2:
            cash2.deQueue()
            count2 = 0
    if not people.isEmpty() or check == 0 :
        if cash1.size() < 5: cash1.enQueue(item)
        else: cash2.enQueue(item)

    if not cash1.isEmpty(): count1 += 1
    if not cash2.isEmpty(): count2 += 1
    # print(people)
    print(i,people.items,cash1.items,cash2.items, sep=" ")



