class Node:
    def __init__(self,data,left=None,right=None):
        self.data = data 
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.data)

def insert(root,data):
    if root ==None:
        return Node(data)
    else:
        if data < root.data:
            root.left = insert(root.left,data)
        else:
            root.right = insert(root.right,data)
        return root

def high(root):
    if root == None:
        return -1
    else:
        hl = high(root.left)
        hr = high(root.right)
        if hl>hr:
            return hl+1
        else:
            return hr+1

root = None
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = insert(root, i)
print('Height of this tree is : {}'.format(high(root)))