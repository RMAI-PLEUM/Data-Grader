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
            s += str(x) + ' '
        return s

# sum = ['a','l','l','m']
# stack1 = Stack(sum)
# print(stack1.pop())
# print(stack1.push('m'))
# print(stack1.push('ight'))
# print(stack1)
