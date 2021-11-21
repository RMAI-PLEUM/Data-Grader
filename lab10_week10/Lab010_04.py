import math
class Hash:
    def __init__(self, tableSize, collision, threshold = 70):
        self.tableSize = tableSize
        self.collision = collision
        self.element = []
        self.table = []
        self.threshold = threshold
        for _ in range(tableSize):
            self.table.append(None)
    
    def getHash(self, key):
        return key % self.tableSize
    
    def numberOfElement(self):
        number = 0
        for i in range(len(self.table)):
            if self.table[i] is not None:
                number += 1
        return number

    def isFull(self):
        return self.numberOfElement() == self.tableSize
    
    def reHash(self, adding=None):
        if adding is not None:
            self.element.append(adding)

        self.table = []

        for possible_prime in range(self.tableSize*2, 99999999999999):  
            for i in range(2, int(math.sqrt(self.tableSize*2))+1):
                if possible_prime % i == 0:
                    break
            else:
                self.tableSize = possible_prime
                break

        for i in range(self.tableSize):
            self.table.append(None)
        for value in self.element:
            retry = 0
            hashed_index = self.getHash(value)
            while retry < self.collision:
                index = (hashed_index + retry ** 2) % self.tableSize
                if self.table[index] is None:
                    self.table[index] = value
                    break
                retry += 1
                print(f'collision number {retry} at {index}')

    def __str__(self):
        out = ''
        for i in range(self.tableSize):
            out += f"#{i+1}\t{self.table[i]}\n"
        out += '----------------------------------------'
        return out

    def insert(self, value):
        print("Add :", value)

        retry = 0
        hashed_index = self.getHash(value)
        while retry < self.collision:
            index = (hashed_index + retry ** 2) % self.tableSize
            if self.table[index] is None:
                if (self.numberOfElement()+1) * 100 / self.tableSize > self.threshold:
                    print("****** Data over threshold - Rehash !!! ******")
                    self.reHash(value)
                else:
                    self.element.append(value)
                    self.table[index] = value
                return
            retry += 1
            print(f'collision number {retry} at {index}')

        print("****** Max collision - Rehash !!! ******")
        self.reHash(value)

print(" ***** Rehashing *****")
control, lst = input("Enter Input : ").split('/')
tableSize, collision, threshold = list(map(int, control.split()))
lst = list(map(int, lst.split()))
print("Initial Table :")
hash = Hash(tableSize, collision, threshold)
print(hash)
for item in lst:
    hash.insert(item)
    print(hash)