
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

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
        if self.root is None:
            self.root = Node(data)
        else:
            curr = self.root
            while True:
                if data < curr.data:
                    if curr.left is None:
                        curr.left = Node(data)
                        break
                    curr = curr.left
                else:
                    if curr.right is None:
                        curr.right = Node(data)
                        break
                    curr = curr.right
        return self.root

    def bfs(self):
        if self.root is None:
            return "Empty Tree"
        q = Queue()
        q.enqueue(self.root)
        out = "Breadth : "
        while not q.is_empty():
            curr = q.dequeue()
            out += str(curr.data) + ' '
            if curr.left is not None:
                q.enqueue(curr.left)
            if curr.right is not None:
                q.enqueue(curr.right)
        return out

pre = 'Preorder : '
post = 'Postorder : '
ino = 'Inorder : '

def preorder(curr):
    global pre
    if curr is not None:
        pre += str(curr.data) + ' '
        preorder(curr.left)
        preorder(curr.right)


def inorder(curr):
    global ino
    if curr is not None:
        inorder(curr.left)
        ino += str(curr.data) + ' '
        inorder(curr.right)


def postorder(curr):
    global post
    if curr is not None:
        postorder(curr.left)
        postorder(curr.right)
        post += str(curr.data)+' '

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
preorder(T.root)
print(pre)
inorder(T.root)
print(ino)
postorder(T.root)
print(post)
print(T.bfs())