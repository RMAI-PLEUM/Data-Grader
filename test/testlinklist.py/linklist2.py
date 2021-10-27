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
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.previous != None:
            s += str(cur.previous.value) + " "
            cur = cur.previous
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
        

    def addHead(self, item):
        new_node = Node(item)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return
        self.head.previous = new_node
        new_node.next = self.head
        self.head = new_node
        self.count += 1
        return

    def insert(self, pos, item):
        new_node = Node(item)
        if pos == 0 :
            self.addHead(item)
            return
        if pos > 0:
            if pos >- self.count:
                self.append(item)
            else:
                p = self.head
                for _ in range(0,pos):
                    p = p.next
                previousnode = p
                nextnode = p.next
                previousnode.next = new_node
                new_node.next = new_node
        else:
            if pos <= -self.size:
                self.addHead(item)
                return
            else:
                node = self.tail
                for _ in range(-1, pos-1, -1):
                    node = node.previous

                previous_node = node
                next_node = previous_node.next

                previous_node.next = new_node
                new_node.previous = previous_node

                next_node.previous = new_node
                new_node.next = next_node

        self.count += 1 

    def search(self, item):
        if self.index(item) != -1:
            return 'Found'
        else: return 'Not Found'

    def index(self, item):
        r = 0
        p = self.head
        while p != None:
            if p.value == item:
                return r
            r += 1
            p = p.next
        return -1


    def size(self):
        return int(self.count)

    def pop(self, pos):
        if self.count-1 < pos or pos < 0:
            return "Out of Range"

        if self.count == 1:
            self.head = None
            self.tail = None

        elif pos == 0:
            print(f"l {self}")
            print("size "+ str(self.count))
            new_head = self.head.next
            new_head.previous = None

            self.head = new_head
            
        elif pos == self.count-1:
            new_tail = self.tail.previous
            new_tail.next = None

            self.tail = new_tail

        else:
            node = self.head
            for _ in range(0, pos):
                node = node.next

            previous_node = node.previous
            next_node = node.next

            if previous_node is not None:
                previous_node.next = next_node
                next_node.previous = previous_node

        self.count -= 1

        return "Success"

L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L)
print("Linked List Reverse :", L.reverse())
# L.append('add')
# L.append('tail')
# L.addHead('head')
# L.addHead('headiek')
# print(L)
# print(L.size())
# print(L.head.value)
# print(L.tail.value)
# print(L.index('add'))
# print(L.search('add'))
