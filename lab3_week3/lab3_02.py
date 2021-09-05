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
    
def match(op,cl):
    opens = "([{"
    closes = ")]}"
    return opens.index(op) == closes.index(cl) 
    
s = Stack()
i = 0         
error = 0
str = input('Enter expresion : ')
while i < len(str) and error == 0 :
    c = str[i]
    if c in '{[(':
        s.push(c)
    else:
        if c in '}])':
            if s.size() > 0:
                 if not match(s.pop(),c):
                     error = 1 	# open & close not match
            else: 	# empty stack 
                   error = 2 	# no open paren
    i += 1

    
if s.size() > 0 and error == 0:  	# stack not empty
    error = 3	# open paren(s) excesses

if error == 1:
    print(str , 'Unmatch open-close  ')
    
elif error == 2:
    print(str , 'close paren excess')
elif error == 3:
    print(str , 'open paren excess  ', s.size(),': ',end=''  ) 
    for ele in s.items:
        print(ele,sep=' ',end = '')
    print()
    
    
else: 
    print(str, 'MATCH')