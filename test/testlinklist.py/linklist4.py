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
            s += str(p.data) + ' '
            p = p.next
        return s

    def value(self):
        s = ''
        p = self.head
        while p != None:
            s += str(p.data) + ' '
            p = p.next
        return s

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
            if self.Indexof(data) == 0 and self.size > 0:
                self.popfont()
                return
            elif self.Indexof(data) == self.size-1:
                self.popback()
                return
            elif self.Indexof(data) > 0 and self.Indexof(data) < self.size-1:
                current_node = self.nodeAt(self.Indexof(data))
                previous_node =  self.nodeAt(self.Indexof(data)-1)
                next_node =  self.nodeAt(self.Indexof(data)+1)
                previous_node.next = next_node
                current_node.next = None
                self.size -= 1
                return
        else:
            print(f'{data} not in Linklist.')
        return
    
    def pop(self, index):
        current_node = self.nodeAt(index)
        previous_node = self.nodeAt(index-1)
        next_node = self.nodeAt(index+1)
        previous_node.next = next_node
        current_node.next = None
        self.size -= 1
        return

text = SinglyLinklist('|')
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[0] == 'I': #เป็นการนำ word ลงไปใส่ในตำแหน่งของ Cursor ปัจจุบัน หลังจากใส่ word เสร็จ ตำแหน่งของ Cursor จะมาอยู่ด้านหลังของ word ที่ใส่ลงไป
        text.insertAfter(text.Indexof('|'), i[2:])
    elif i[0] == 'L': #:   เป็นการเลื่อน Cursor จากตำแหน่งปัจจุบันไปทางด้านซ้าย 1 ตำแหน่ง 
        index = text.Indexof('|')
        text.remove('|')
        if index <= 0:
            text.insertAfter(0, '|')
        if index > 0:
            text.insertAfter(index-1, '|')
    elif i[0] == 'R': #   เป็นการเลื่อน Cursor จากตำแหน่งปัจจุบันไปทางด้านขวา 1 ตำแหน่ง
        if '|' in text.value() and text.size == 2:
            text.remove('|')
            text.pushback('|')
        elif '|' in text.value() and text.size > 1:
            index = text.Indexof('|')
            text.remove('|')
            if index >= text.size-1:
                text.insertAfter(text.size-1,'|')
            if index < text.size:
                text.insertAfter(index+1,'|')
        
    elif i[0] == 'B': # เป็นการลบ word 1 ตัวทางด้านซ้ายของ Cursor 
        index = text.Indexof('|')
        if index > 0:
            text.pop(index-1)
    elif i[0] == 'D': #เป็นการลบ word 1 ตัวทางด้านขวาของ Cursor
        index = text.Indexof('|')
        if index < text.size-1:
            text.pop(index+1)
print(text)

# test = SinglyLinklist(['Apple','Bird', 'Cat','|'])
# index = test.Indexof('|')
# test.remove('|')
# test.insertAfter(index-1, '|')
# index = test.Indexof('|')
# test.remove('|')


# print(test)
# print(index)