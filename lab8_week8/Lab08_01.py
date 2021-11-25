class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        newNode = Node(data)
        if self.root is None:
            self.root = newNode
            print('*', end='')
        else:
            currentNode = self.root
            while currentNode is not None:
                if data > currentNode.data:
                    print('R', end='')
                    if currentNode.right is None:
                        currentNode.right = newNode
                        print('*', end='')
                        break

                    currentNode = currentNode.right

                elif data < currentNode.data:
                    print('L', end='')
                    if currentNode.left is None:
                        currentNode.left = newNode
                        print('*', end='')
                        break
                    currentNode = currentNode.left

        print()
        return self.root

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

inp = [int(i) for i in input('Enter Input : ').split()]
t = BinarySearchTree()
for i in inp:
    root = t.insert(i)

t.printTree(root)