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


input_val = input("Enter people and time : ").split()
ls = [i for i in input_val[0]]
q0 = Queuelist(ls)
q1 = Queuelist()
q2 = Queuelist()

# count1 = 0
# count2 = 0
# check = 0
# for i in range(1, int(input_val[1]) + 1):
#     item = ""
#     if q0.isEmpty() == False: item += q0.deQueue()
#     else: check += 1
    
#     if i > 2:
#         if count1 == 3: 
#             q1.deQueue()
#             count1 = 0
#         if count2 == 2: 
#             q2.deQueue()
#             count2 = 0
            
#     if q0.isEmpty() == False or check == 0:
#         if q1.size() < 5: q1.enQueue(item)
#         else: q2.enQueue(item)
    
#     if q1.isEmpty() == False: count1 += 1
#     if q2.isEmpty() == False: count2 += 1
#     print(i, q0.items, q1.items, q2.items, sep = " ")