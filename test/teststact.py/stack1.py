class Stack:
    def __init__(self, list = None):
        if list is None:
            self.item = []
        else:
            self.item = list

    def isEmpty(self):
        return self.size() == 0
    
    def push(self, data):
        return self.item.append(data)
    
    def pop(self):
        return self.item.pop()

    def peek(self):
        return self.item[-1]
    
    def size(self):
        return len(self.item)

    def __str__(self):
        s = ''
        for x in self.item:
            s += str(x) + ' '
        return s

stack = Stack()
inp = input("Enter input : ").split(',')
for i in inp:
    if 'A' in i:
        stack.push(int(i[2:]))
        print(f'Add = {i[2:]} and Size = {stack.size()}')
    elif 'P' in i:
        if stack.size() != 0:
            print(f'Pop = {stack.pop()} and Index {stack.size()}')
        else:
            print(-1)

if stack.isEmpty():
    print(f'Value in Stack = Empty')

else:
    print(f'Value in Stack = {stack}')
        
        