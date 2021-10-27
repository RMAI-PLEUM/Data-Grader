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
            s += str(p.data) + '->'
            p = p.next
        return s[:-2]

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
        # if index == self.size - 1:
        #     self.pushback(data)
        #     return
            
        else: 
            p = self.nodeAt(index-1)
            new_node = Node(data)
            new_node.next = self.nodeAt(index)
            p.next = new_node
            self.size += 1
        return 

    def remove(self, data):
        if self.isIn(data):
            if self.Indexof(data) == 0:
                self.popfont()
                return
            elif self.Indexof(data == self.size - 1):
                self.popback()
                return
            else:
                current_node = self.nodeAt(self.Indexof(data))
                p = self.nodeAt(self.Indexof(data)-1)
                conti = self.nodeAt(self.Indexof(data)+1)
                if self.Indexof(conti.data) == self.size:
                    self.popback()
                    return
                else:
                    current_node.next = None
                    p.next = conti
                    self.size -= 1
        else:
            print(f'{data} not in Linklist.')
        return

inp = input('Enter Input : ').split(',')
l = SinglyLinklist(inp[0].split())

if(inp[0] == ' '):
    print('List is empty')
else :
    print(f'link list : {l}')

for i in range(1,len(inp)):
    inp[i].split(':')
    buffer = inp[i].split(':')
    index = int(buffer[0])
    data = int(buffer[1])
    
    if index >= 0 and index <= len((l)):
            l.insertAfter(index, data)
            print(f'index = {index} and data = {data}')
            if (l.isEmpty()):
                print('List is empty')
            else:
                print(f'link list : {l}')
    else:
            print('Data cannot be added')

if (l.isEmpty()):
                print('List is empty')
