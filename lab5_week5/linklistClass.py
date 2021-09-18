class SinglyLinkedList :
    class Node:
        def __init__(self, data, next = None):
            self.data = data
            if next is None:
                self.next = None
            else: self.next = next
        
    def __init__(self):
        self.head = None
        self.size = 0

    def __str__(self):
        s = ''
        p = self.head
        while p != None:
            s += str(p.data) + ' '
            p = p.next
        return s
    
    def __len__(self):
        return self.size

    def isEmty(self):
        return self.size == 0

    def indexOf(self, data):
        p = self.head
        for i in range(len(self)):
            if p.data == data:
                return i
            p = p.next
        return -1
    
    def isIn(self, data):
        return self.indexOf(data) >= 0

    def nodeAt(self, index):
        p = self.head
        for j in range(0, index):
            p = p.next
        return p

    def insertAfter(self, i, data):
        q = self.nodeAt(i)
        p = self.Node(data)
        p.next = q.next
        q.next = p
        self.size += 1

    def append(self, data):
        if self.head is None:
            p = self.Node(data)
            self.head = p
            self.size += 1
        else: 
            self.insertAfter(len(self)-1, data)
            

    def deleteAfter(self, i):
        if self.size > 0:
            q = self.nodeAt(i)
            q.next = q.next.next
            self.size -= 1
        
    def delete(self, i):
        if i == 0 and self.size > 0:
            self.head = self.head.next
            self.size -= 1
        else: self.deleteAfter(i-1)

    def removeData(self, data):
        if self.isIn(data):
            self.deleteAfter(self.indexOf(data)-1)

    def addHead(self, data):
        if self.isEmty():
            p = self.Node(data)
            self.head = p
            self.size += 1
        else: 
            p = self.Node(data,self.head)
            self.head = p
            self.size += 1



p = SinglyLinkedList()
p.addHead(0)
p.append(1)
p.append(4)
print