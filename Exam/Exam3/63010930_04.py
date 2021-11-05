class Node:
    def __init__(self, data):
        self.data  = data
        self.right = None
        self.left = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def create(self, data):
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

def height(obj):
    if obj == None:
        return -1
    else:
        highL = height(obj.left)
        highR = height(obj.right)
        if highL > highR:
            return highL+1
        else:
            return highR+1



print(" *** Binary Search Tree Height ***")

tree = BinarySearchTree()

arr = list(map(int, input("Enter Input : ").split()))

for e in arr:

    tree.create(e)

print("Height = ",height(tree.root),end="\n\n")
