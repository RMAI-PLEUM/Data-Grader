class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class Hash:

    def __init__(self, tableSize, collision):
        self.tableSize = tableSize
        self.collision = collision
        self.table = []
        for _ in range(tableSize):
            self.table.append(None)
        
    def getHash(self, key):
        index = 0
        for c in key:
            index += ord(c)
        return index % self.tableSize
    
    def isFull(self):
        count = 0
        for i in range(len(self.table)):
            if self.table[i] is not None:
                count += 1
        return count == self.tableSize

    def insert(self, data):
        if self.isFull():
            print("This table is full !!!!!!")
            quit()
        key, value = data.key, data.value
        retry = 0
        hashed_index = self.getHash(key)
        while retry < self.collision:
            index = (hashed_index + retry ** 2) % self.tableSize
            if self.table[index] is None:
                self.table[index] = data
                return
            retry += 1
            print(f'collision number {retry} at {index}')

        print("Max of collisionChain")

    def __str__(self):
        out = ''
        for i in range(self.tableSize):
            out += f"#{i+1}\t{self.table[i]}\n"
        out += '---------------------------'
        return out

print(" ***** Fun with hashing *****")
control, lst = input('Enter Input : ').split('/')
tbSize, collision = list(map(int, control.split()))
lst = lst.split(',')
data = []
for i in lst:
    key, value = i.split()
    data.append(Data(key, value))

hash = Hash(tbSize, collision)
for i in data:
    hash.insert(i)
    print(hash)
