class Node:
    def __init__(self, value, next = None, prev = None):
        self.value = value
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self, lst=None):
        self.head = None
        self.tail = None 
        if lst != None:
            for item in lst:
                self.append(item)
    
    def isEmpty(self):
        return self.head == None

    def size(self):
        current_node = self.head
        count = 0
        while current_node is not None:
            count += 1
            current_node = current_node.next
        return count

    def append(self, value):
        new_node = Node(value)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
            return
        else:
            self.tail.next = Node(value, prev = self.tail)
            self.tail = self.tail.next
    
    def addHead(self, value):
        if self.head == None :
            self.head = Node(value)
            self.tail = self.head
            return 
        else:
            new_node = Node(value , self.head)
            self.head.prev = new_node
            self.head = new_node
        
    def pop(self):
        if self.isEmpty():
            print('List is empty')
            return -1
        last = self.tail
        self.tail = last.prev
        if self.tail is not None:
            self.tail.next = None
        last.prev = None
        if self.tail is None:  
            self.head = None
        return last.value
            
    
    def __str__(self):
        current_node = self.head
        s = ''
        while current_node != None:
            s += current_node.value+' '
            current_node = current_node.next
        return s

inp = input('Enter Input (L1,L2) : ').split()
lis1 = inp[0].split('->')
lis2 = inp[1].split('->')
l1 = LinkedList(lis1)
l2 = LinkedList(lis2)
print('L1    :', l1)
print('L2    :', l2)
merge = LinkedList(lis1)
count = l2.size()
for i in range(0,count):
    merge.append(l2.pop())
print("Merge :",merge)




