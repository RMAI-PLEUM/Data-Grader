class Queuelist:

    def __init__(self, Q = None):
        if Q == None:
            self.items = []
        else:
            self.items = Q
    
    def enQueue(self,i):
        self.items.append(i)

    def deQueue(self):
        return self.items.pop(0)

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
 
    def value(self):
        ch = ''
        i = 0
        for i in range(len(self.items)):
            ch += str(self.items[i])+' ' 
        return ch
    
    def first(self):
        return self.items[0]

act = {'0':'Eat','1':'Game','2':'Learn','3':'Movie'}
place = {'0':'Res.','1':'ClassR.','2':'SuperM.','3':'Home'}
day = []
day = input("Enter Input : ").split(',')
# print(day)
myq = []
yourq = []
i = 0

for i in range(len(day)):
    m = ''
    y = ''
    m , y = day[i].split(' ')
    myq.append(m)
    yourq.append(y)

# print(myq)
# print(yourq)
mych = ''
for i in range(len(myq)):
    if i == len(myq)-1:
        mych+= myq[i]
    else:
     mych += myq[i]+", "
yourch = ''
for i in range(len(yourq)):
    if i == len(yourq)-1:
        yourch+= yourq[i]
    else:
     yourch += yourq[i]+", "

print("My   Queue =",mych)
print("Your Queue =",yourch)
myact = []
mylo = []
for i in range(len(myq)):
    ca = ''
    cl = ''
    ca ,cl = myq[i].split(':')
    myact.append(ca)
    mylo.append(cl)
maml = ''
for i in range(len(myact)):
    if i == len(myact)-1:
        maml+= act[myact[i]]+":"+place[mylo[i]]
    else:
     maml += act[myact[i]]+":"+place[mylo[i]]+", "
print("My   Activity:Location = "+maml)
youract = []
yourlo = []
for i in range(len(myq)):
    ca = ''
    cl = ''
    ca ,cl = yourq[i].split(':')
    youract.append(ca)
    yourlo.append(cl)
yayl = ''
for i in range(len(youract)):
    if i == len(youract)-1:
        yayl+= act[youract[i]]+":"+place[yourlo[i]]
    else:
     yayl += act[youract[i]]+":"+place[yourlo[i]]+", "
print("Your Activity:Location = "+yayl)

myAct = Queuelist(myact)
myLo = Queuelist(mylo)
yourAct = Queuelist(youract)
yourLo = Queuelist(yourlo)
point = 0

for i in range(myAct.size()):
    if (myAct.first() != yourAct.first() and myLo.first() != yourLo.first()):
     point-= 5
    if (myAct.first() == yourAct.first() and myLo.first() == yourLo.first()):
     point+= 4
    if (myAct.first() != yourAct.first() and myLo.first() == yourLo.first()):
     point+= 2
    if (myAct.first() == yourAct.first() and myLo.first() != yourLo.first()):
     point+= 1

    myAct.deQueue()
    myLo.deQueue()
    yourAct.deQueue()
    yourLo.deQueue()

if point < 0:
    print("No! We're just friends. : Score is {}.".format(point))
elif point>0 and point<7:
    print("Umm.. It's complicated relationship! : Score is {}.".format(point)) 
elif point >= 7:
    print("Yes! You're my love! : Score is {}.".format(point))
    