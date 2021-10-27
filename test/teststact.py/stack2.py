class Stack:
    def __init__(self, list = None):
        if list is None:
            self.item = []
        else:
            self.item = list

    def isEmpty(self):
        return len(self.item) is None
    
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
            s += str(x)
        return s

stackp = Stack()
stackc = Stack()
open = '([{'
close = ')]}'
t = input('Enter expresion : ')
inp = ''
for i in t:
    if i in open or i in close:
        inp += i
for i in inp:
    if i in open:
        stackp.push(i)
    if i in close:
        if stackp.size() != 0:
            if close.index(i) == open.index(stackp.peek()):
                stackp.pop()
            else:
                stackc.push(i)
        else: stackc.push(i)
        

if stackp.size() != 0 and stackc.size() != 0:
    print(inp, 'Unmatch open-close')
    exit(0)
if stackp.size() == 0 or stackc.size() == 0:
    if stackp.size() > 0:
        print(f'{inp} open paren excess   {stackp.size()} : {stackp}')
    if stackc.size() > 0:
        print(f'{inp} close paren excess')
print(stackp)
print(stackc)

