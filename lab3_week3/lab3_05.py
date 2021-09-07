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
        s = ''
        for ele in self.items:
            s += str(ele)+' '
        return s

print("******** Parking Lot ********")

m,s,o,n = input("Enter max of car,car in soi,operation : ").split()
m,n = int(m),int(n)
ns = ''
i = 0 
while i < len(s):
    if (s[i] not in ","):
        ns+=s[i]
    i+=1
ns = list(map(int,ns))
S = Stack(ns)
# print(S.value())

if(o in "arrive"):
    if (n not in S.items):
     if (0 in S.items):
         print("car {} arrive! : Add Car {}".format(n,n))
         S.pop()
         S.push(n)
         print(S.items)
         exit()
     if n <= m:
        print("car {} arrive! : Add Car {}".format(n,n))
        S.push(n)
        print(S.items)
        exit()
     if n > m:
         print("car {} cannot arrive : Soi Full".format(n))
         

    

    if (n in S.items):
        print("car {} already in soi".format(n))
if(o in "depart"):
     if (0 in S.items):
         print("car {} cannot depart : Soi Empty".format(n,n))
         S.pop()
         print(S.items)
         exit()
     if (n not in S.items):
         print("car {} cannot depart : Dont Have Car {}".format(n,n))
     if (n in S.items):
         print("car {} depart ! : Car {} was remove".format(n,n))
         S.items.remove(n)


    

# print("{} {} {} {}".format(m,ns,o,n))
print(S.items)
