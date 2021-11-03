class Node:
    def __init__(self, data):
        self.data  = data
        self.right = None
        self.left = None
    
    def __str__(self):
        return str(self.data)
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)   
    
class BST:
    def __init__(self):
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

    def delete(self,root,data):
        ### Base Case ###
        if root is None:
            return root

        ### Recursion Case ###
        if data < root.data:
            root.left = self.delete(root.left, data)
        if data > root.data:
            root.right = self.delete(root.right, data)

        ### Found Deleted Node ###
        if data == root.data:
            # Node with [0,1] child
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            # Node with [2] child : Use inorder successor
            else:
                # successor = node that cotent smallest data in the right subtree
                successor = self.getMinNode(root.right)

                # Replace root.data with the successor
                root.data = successor.data

                # Delete node that content the successor
                root.right = self.delete(root.right, successor.data)
                
        return root


    def getMax(self):
        p = self.root
        if p == None:
            return None
        else:
            while p.right != None:
                p = p.right
            return p.data

    def getMaxNode(self, root):
        p = root
        if p == None:
            return None
        else:
            while p.right != None:
                p = p.right
            return p
    
    def getMin(self):
        p = self.root
        if p == None:
            return None
        else:
            while p.left != None:
                p = p.left
            return p.data

    def getMinNode(self, root):
        p = root
        if p == None:
            return None
        else:
            while p.left != None:
                p = p.left
            return p

    def findData(self, node, data):
        if node == None:
            return 0
        elif node.data > data:
            return self.findData(node.left, data)
        return 1 + self.findData(node.left, data) + self.findData(node.right, data)

    def BFS(self):
        if self.root == None:
            return 'Empty Tree'
        q = Queue()
        q.enqueue(self.root)
        s = 'Breadth : '
        while not q.is_empty():
            p = q.dequeue()
            s += str(p.data) + ' '
            if p.left != None:
                q.enqueue(p.left)
            if p.right != None:
                q.enqueue(p.right)
        return s
    
    def preorder(self,node):
        if node == None:
            return
        print(node.data,end=" ")
        self.preorder(node.left)
        self.preorder(node.right)

    def postorder(self,node):
        if node == None:
            return 
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.data,end=" ")

    def inorder(self,node):
        if node is None:
            return
        self.inorder(node.left)
        print(node.data,end = " ")
        self.inorder(node.right)

    def displayOrder(self):
        print('Preorder : ',end='')
        self.preorder(self.root)
        print('\nInorder : ',end='')
        self.inorder(self.root)
        print('\nPosorder : ', end='')
        self.postorder(self.root)
        print('\n', end='')
        print(self.BFS())    
    
    def highTree(self, node):
        if node == None:
            return -1
        else: 
            hL = self.highTree(node.left)
            hR = self.highTree(node.right)
            if hL > hR:
                return hL+1
            else:
                return hR+1

    def highData(self, node, data):
        if node.data == data:
            return self.highTree(node)
        else:
            if data > node.data:
                return self.highData(node.right, data)
            else:
                return self.highData(node.left, data)

    def depthData(self, node, data):
        if node.data == data:
            return 0
        else:
            if data < node.data:
                return 1+self.depthData(node.left, data)
            else:
                return 1+self.depthData(node.right, data)
    
    def search(self, node, data):
        if node == None:
            return None
        elif node.data == data:
            return data
        else:
            if data < node.data:
                return self.search(node.left, data)
            else:
                return self.search(node.right, data)

    def checkposition(self, data):
        if self.root == None:
            print('Not exist')
            return
        if self.root.data == data:
            print('Root')
            return
        p = self.root
        while p != None:
            if data == p.data:
                if p.left == None and p.right == None:
                    print('Leaf')
                    return
                else:
                    print('Inner')
                    return
            elif data > p.data:
                p = p.right
            else:
                p = p.left
        print('Not exist')
    
    def father(self, node, data):
        if node == None:
            return 'Tree is empty'
        if node.data == data:
            return f'Not because {data} is Root'
        else:
            p = node
            while p.right != None or p.left != None:
                if p.right != None and p.right.data == data:
                    return p.data
                elif p.left != None and p.left.data == data:
                    return p.data
                else:
                    if data >= p.data:
                        p = p.right
                    else: p = p.left
        return 'Not found data'

    def path(self, node, data):
        if node.data == data:
            print(node.data)
            return node
        else:
            if data < node.data:
                print(node.data,end=' ')
                return self.path(node.left, data)
            else:
                print(node.data,end=' ')
                return self.path(node.right, data)            


    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)



T = BST()
test = '15 5 20 3 -1 7 9 30 1 100 10'
inp = [int(i) for i in test.split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)
T.path(root,-1)



