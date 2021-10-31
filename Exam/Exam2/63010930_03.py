class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def __str__(self):
        if self.isEmpty():
            return 
        current_node = self.head
        s = str(self.head.value) + ' '

        while current_node.next != None:
            s += str(current_node.next.value) + " "
            current_node = current_node.next
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        new_node = Node(item)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            self.count += 1
            return
        new_node.previous = self.tail
        self.tail.next = new_node
        self.tail = new_node
        self.count += 1
        return

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.previous != None:
            s += str(cur.previous.value) + " "
            cur = cur.previous
        return s

inp = input('Enter numbers : ').split()

ll = LinkedList()
for i in inp:
    ll.append(i)

print("Linkedlist Before Reverse")
print(f'Linked data : {ll}')
print("Linkedlist After Reverse")
print(f'Linked data : {ll.reverse()}')
