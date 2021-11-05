class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)
class BST:
    def __init__(self) :
        self.root = None

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            p = self.root
            while True:
                if data >= p.data:
                    if p.right == None:
                        p.right = Node(data)
                        break
                    else:
                        p = p.right
                elif data < p.data:
                    if p.left == None:
                        p.left = Node(data)
                        break
                    else:
                        p = p.left
        return self.root

    def printTree(self, node, level = 0):

        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
    
    def max(self):
        p = self.root
        while p.right != None:
            p = p.right
        return p.data

    def min (self):
        p = self.root
        while p.left != None:
            p = p.left
        return p.data

T = BST()

inp = [int(i) for i in input('Enter Input : ').split()]

for i in inp:

    root = T.insert(i)

T.printTree(root)

print('-' * 50)
print(f'Min : {T.min()}')
print(f'Max : {T.max()}')