class Node:
    def __init__(self, data, next = None):
        self.data = data
        if next == None:
            self.next = None
        else:
            self.next = next

class SinglyLinklist:
    def __init__(self, list = None):
        self.head = None
        self.tail = None
        self.size  = 0
        if list is not None:
            for i in list:
                self.pushback(i)
        return 
    
    def __str__(self):
        s = ''
        p = self.head
        while p != None:
            s += str(p.data) + ' <- '
            p = p.next
        return s[:-3]

    def __len__(self):
        return self.size

    def pushback(self, data):
        if self.size == 0:
            new_node = Node(data,None)
            self.head = new_node
        else:
            new_node = Node(data)
            p = self.head
            while p.next != None:
                p = p.next
            p.next = new_node
            self.tail = new_node
            
        self.size += 1
        return 
    
    def pushfront(self, data):
        if self.size == 0:
            new_node = Node(data,None)
            self.head = new_node
        else:
            new_node = Node(data,self.head)
            self.head = new_node
        self.size +=1
        return

    def popfont(self):
        if self.size == 0:
            print('linklist is empty.')
            return 
        if self.size == 1:
            self.head = None
            self.tail = None
            self.size = 0
        else:
            p = self.head
            self.head = self.head.next
            p.next = None
            self.size -= 1

    def popback(self):
        if self.size == 0:
            print('linklist is empty.')
            return 
        if self.size == 1:
            self.head = None
            self.tail = None
            self.size = 0
        else:
            i = self.size -1
            p = self.nodeAt(i-1)
            p.next = None
            self.tail = p
            self.size -= 1

    def Indexof(self, data):
        if self.size == 0:
            print('linklist is empty.')
        else:
            p = self.head
            index = 0
            while p != None:
                if p.data == data:
                    return index
                index += 1
                p = p.next
            return -1
        return 
    
    def nodeAt(self, index):
        p = self.head
        for _ in range(index):
            p = p.next
        return p

    def isEmpty(self):
        return self.size == 0

    def isIn(self, data):
        if self.Indexof(data) > -1:
            return True
        else: 
            return False

    def insertAfter(self, index, data):
        if index == 0:
            self.pushfront(data)
            return
        else: 
            p = self.nodeAt(index-1)
            new_node = Node(data)
            new_node.next = self.nodeAt(index)
            p.next = new_node
            self.size += 1
        return

    def order(self):
        if self.head != '0':
            p = self.head
            while p.data != '0':
                p = p.next
            zero_node = self.nodeAt(self.Indexof(p.data))
            last = self.head
            while last.next != None:
                last = last.next

            previous0_node = self.nodeAt(self.Indexof(p.data) - 1)
            previous0_node.next = None
            last.next = self.head
            self.head = zero_node
            self.tail = previous0_node
            return self

        
        

print(' *** Re order ***')
inp = input('Enter Input : ').split()
l = SinglyLinklist()

for i in inp:
    l.pushback(i)

print(f'Before : {l}')
if l.head.data != '0':
    print(f'After : {l.order()}')
else:
    print(f'After : {l}')







