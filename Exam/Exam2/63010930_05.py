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

    def __len__(self):
        return self.size

    def pushback(self, data):
        current_node = self.head
        p = Node(data)
        if self.head == None:
            self.head = self.tail = p
            return
        elif self.head.data > data:
            p.next = self.head
            self.head = p
            return

        while current_node.next is not None:
            if current_node.next.data > data:
                break
            current_node = current_node.next
        p.next = current_node.next
        current_node.next = p
        return
    
    
    def nodeAt(self, index):
        p = self.head
        for _ in range(index):
            p = p.next
        return p

    def isEmpty(self):
        return self.size == 0

    def findMean(self):
        count = 0
        p = self.head
        while p != None:
            count += p.data
            p = p.next
        count/len(self)
        mean = count/len(self)
        return mean
    
    def findMedian(self):
        n = len(self)
        if n%2 == 1:
            n = int((n/2)+ 0.5)
            p = self.head
            for _ in range(n-1):
                p = p.next
            return p.data
        if n%2 == 0:
            n = n/2
            nL = int(n- 0.5)
            nR = int(n+ 0.5)
            l = self.head
            for _ in range(nL):
                l = l.next 
            r = self.head
            for _ in range(nR):
                r = r.next
            median  = (l.data + r.data)/2
            return median

    def __len__(self):
        p = self.head
        count = 0
        while p != None:
            count += 1
            p = p.next
        return count



inputlist = [int(e) for e in input('Enter numbers : ').split()]

l = SinglyLinklist()
for i in inputlist:
    l.pushback(i)


print("Output :")
print(f'Linked data : {l}')
print('Amount of data =',len(l))
print('Mean = {:.2f}'.format(l.findMean()))
print('Median = {:.2f}'.format(l.findMedian()))


