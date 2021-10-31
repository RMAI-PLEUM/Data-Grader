class Stack:
    def __init__(self, list = None):
        if list is None:
            self.item = []
        else:
            self.item = list

    def __str__(self):
        s = ''
        for x in self.item:
            s += str(x) + ' '
        return s

    def push(self, data):
        return self.item.append(data)

    def pop(self):
        return self.item.pop()

    def isEmpty(self):
        return len(self.item) is None

    def size(self):
        return len(self.item)

    def peek(self):
        return self.item[-1]

    def bottom(self):
        return self.item[0]

inp = int(input('Enter choice : '))

if inp == 1:
    s1 = Stack()
    s1.push(10)
    s1.push(20)
    print(f'Data in Stack is : {s1}')
    s1.pop()
    s1.push(30)
    print("Peek of stack :",s1.peek())
    print("Bottom of stack :",s1.bottom())

elif inp == 2:
    s1 = Stack()
    s1.push(100)
    s1.push(200)
    s1.push(300)
    s1.pop()
    print(f'Data in Stack is : {s1}')

    print("Stack is Empty :",s1.isEmpty())

elif inp == 3:
    s1 = Stack()
    s1.push(11)
    s1.push(22)
    s1.push(33)
    s1.pop()
    print(f'Data in Stack is : {s1}')

    print("Stack size :",s1.size())