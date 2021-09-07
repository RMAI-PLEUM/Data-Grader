class Stack:
    def __init__(self,list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
    
    def push(self,i):
        self.items.append(i)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
    
    def value(self):
        s = ' '
        for ele in self.items:
            s += str(ele)+' '
        return s


Operators= set(['+', '-', '*', '/', '(', ')', '^'])  
Priority = {'+':1, '-':1, '*':2, '/':2} 

def infix2postfix(exp):

    s = Stack()
    output = ''

    for ch in exp:
        if ch not in Operators:  
            output+= ch

        elif ch=='(':  
            s.push('(')

        elif ch==')':
            while s.items and s.peek() != '(':
                output+=s.pop()
            s.pop()
        else: 
            while s.items and s.peek() !='(' and Priority[ch]<=Priority[s.peek()]:
                output+=s.pop()
            s.push(ch)
    while s.items:
        output+=s.pop()
    return output

print(" ***Infix to Postfix***")

token = input("Enter Infix expression : ")

print("PostFix : ")

print(infix2postfix(token))

