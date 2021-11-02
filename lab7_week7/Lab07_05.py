class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
            return
        else: 
            p = self.root
            while True:
                if data >= p.data:
                    if p.right == None:
                        p.right = Node(data)
                        break
                    else:
                        p = p.right
                if data < p.data:
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
    
    def checkpos(self, data):
        p = self.root
        if p == None:
            print('Not exist')
            return
        
        if p.data == data:
            print('Root')
            return
        
        while p != None:
            if data == p.data:
                if p.left == None and p.right == None:
                    print('Leaf')
                else:
                    print('Inner')
                return
            elif data > p.data:
                p = p.right
            else:
                p = p.left
        print('Not exist')


T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in range(1, len(inp)):
    root = T.insert(inp[i])
T.printTree(root)
T.checkpos(inp[0])