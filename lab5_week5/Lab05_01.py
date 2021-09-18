class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


class LinkedList:
    def __init__(self, lst=None):
        self.head = None
        self.tail = None
        if lst is not None:
            for item in lst:
                self.push_back(item)

    def is_empty(self):
        return self.head is None 

    def size(self):
        current_node = self.head
        count = 0
        while current_node is not None:
            count += 1
            current_node = current_node.next
        return count

    def push_front(self, value):
        if self.is_empty():
            self.head = Node(value)
            self.tail = self.head
            return
        else:
            current_node = Node(value, self.head)
            self.head.prev = current_node
            self.head = current_node

    def push_back(self, value):
        if self.is_empty():
            self.head = Node(value)
            self.tail = self.head
            return
        else:
            self.tail.next = Node(value, prev=self.tail)
            self.tail = self.tail.next

    def insert(self, index, value): 
        if 0 <= index <= self.size():
            if index == 0:
                print("index = {} and data = {}".format(index,value))
                self.push_front(value)
            elif index == self.size():
                print("index = {} and data = {}".format(index,value))
                self.push_back(value)
            else:
                print("index = {} and data = {}".format(index,value))
                count = 0
                current_node = self.head
                while current_node is not None and count != index:
                    current_node = current_node.next
                    count += 1
                prev = current_node.prev
                new_node = Node(value, current_node, prev)
                prev.next = new_node
                current_node.prev = new_node
        else:
            print('Data cannot be added')

    def __str__(self):
        if self.is_empty():
            return 'List is empty'
        else:
            current_node = self.head
            s = 'link list : '
            while current_node is not None:
                s += str(current_node.value)
                if current_node.next is not None:
                    s += '->'
                current_node = current_node.next
            return s


inp = input('Enter Input : ').split(',')
lst = inp[0].split()
l = LinkedList(lst)
print(l)
for i in range(1,len(inp)):
    inp[i] = inp[i].strip()
    index , value = inp[i].split(':')
    index = int(index)
    value = int(value)
    l.insert(index, value)
    print(l)

