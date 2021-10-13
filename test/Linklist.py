class Node:
    def __init__(self, data, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next

class Linklist:
    def __init__(self, list = None):
        
        self.head = None
        self.tail = None
        self.size = 0
        if list is not None:
            for i in list:
                self.pushback(i)
        return 
    
    def pushback(self, data):
        if self.head == None:
            new_node = Node(data)
            self.head = new_node
            self.tail = self.head
            self.size += 1
        else:
            new_node = Node(data)
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.size += 1
        return
    
    def pushfont(self, data):
        if self.head == None:
            new_node = Node(data)
            self.head = new_node
            self.tail = self.head
            self.size += 1
        else:
            new_node = Node(data, next=self.head)
            self.head.prev = new_node
            self.head = new_node
            self.size += 1
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
            self.head = self.head.next
            self.head.prev = None
            self.size -= 1
        return
    
    def popback(self):
        if self.size == 0:
            print('linklist is empty')
            return
        if self.size == 1:
            self.head = None
            self.tail = None
            self.size = 0
        else: 
            self.tail = self.tail.prev
            self.tail.next = None
            self.size -= 1
        return

    def remove(self, data):
        if self.Isin(data) == False:
            print(data, 'not in linklist')
        else:
            if (self.size != 0):
                p = self.head
                for x in range(self.size):
                    if p.data == data:
                        current = p
                        if current == self.head:
                             self.popfont()
                             break
                        if current == self.tail:
                             self.popback()
                             break
                        else:
                            pass
                             
                    p = p.next
        return

    def nodeAt(self, data):
        if self.size > 0 :
            p = self.head
            for i in range(self.size):
                if p.data == data:
                    return p
                p = p.next
        return -1

    def Isin(self, data):
        if self.size == 0:
            return False
        else:
            p = self.head
            for x in range(self.size):
                if data == p.data:
                    return True
                p = p.next
            return False

    def Size(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def indexOF(self, data):
        count = 0
        p = self.head
        for x in range(self.size):
            
            if data == p.data:
                return count
            count += 1
            p = p.next
        return -1

    def __str__(self):
        s = ''
        p = self.head
        for x in range(self.size):
            s += p.data + ' '
            p = p.next
        return s

list = ['m','y','l']
link = Linklist()
link.pushback('khdoifhoehf')
print(link)
link.pushfont('555')
print(link)
link.pushback('miss')
link.popfont()
link.popback()
print(link.size)
print(link)
link.pushback('you')
print(link)
print(link.indexOF('you'))
link.pushfont('same')
link.pushback('hello')
print(link)
link.remove('you')
print(link)



