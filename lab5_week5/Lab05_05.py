
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

def createLL(LL):
    new_node = Node(LL[0])
    head = new_node
    for value in LL[1:]:
        new_node.next = Node(value)
        new_node = new_node.next
    return head

def printLL(head):
    s = ''
    while head !=  None:
        s += f"{head.value} "
        head = head.next
    return s

def SIZE(head):
    count = 0
    while head != None:
        count += 1
        head = head.next
    return count

def bottomUp(head, split):
    old_head = head
    new_tail = head
    for _ in range(0, split-1):
        new_tail = new_tail.next
    new_head = new_tail.next
    new_tail.next = None

    old_tail = new_head
    while old_tail.next is not None:
        old_tail = old_tail.next
    old_tail.next = old_head
    return new_head

def riffle(head, split):
    n = head
    for _ in range(0, split-1):
        n = n.next
    de_head = n.next
    n.next = None
    new_head = head
    p = head
    q = de_head
    while p.next is not None and q.next is not None:
        p_temp = p.next
        q_temp = q.next
        q_next = p.next
        p.next = q
        q.next = q_next
        p = p_temp
        q = q_temp
    if p.next is not None:
        q_next = p.next
        p.next = q
        q.next = q_next
    else:
        p.next = q
    return new_head

def straight(head, complement):
    for _ in range(0, complement-1):
        if int(head.value)+1 != int(head.next.value):
            return False 
        head = head.next
    return True

def scarmble(head, b, r, size):
    b_split = int(size * b/100)
    r_split = int(size * r/100)

    head = bottomUp(head, b_split)
    print(f"BottomUp {b:.3f} % : {printLL(head)}")

    head = riffle(head, r_split)
    print(f"Riffle {r:.3f} % : {printLL(head)}")

    while not straight(head, size-b_split):
        head = riffle(head, r_split)
    print(f"Deriffle {r:.3f} % : {printLL(head)}")

    head = bottomUp(head, size - b_split)
    print(f"Debottomup {b:.3f} % : {printLL(head)}")

inp1, inp2 = input('Enter Input : ').split('/')
print('-' * 50)
h = createLL(inp1.split())
for i in inp2.split('|'):
    print("Start : {0}".format(printLL(h)))
    k = i.split(',')
    if k[0][0] == "B" and k[1][0] == "R":
        scarmble(h, float(k[0][2:]), float(k[1][2:]), SIZE(h))
    elif k[0][0] == "R" and k[1][0] == "B":
        scarmble(h, float(k[1][2:]), float(k[0][2:]), SIZE(h))
    print('-' * 50)