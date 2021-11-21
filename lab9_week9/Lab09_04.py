def sortAlphabet(list):
    l = []
    for i in list:
        l.append((findAlphabet(i), i))
    for i in range(len(list)-1):
        swap = False
        for j in range(len(list)-1-i):
            if l[j][0] > l[j+1][0]:
                l[j], l[j+1] = l[j+1], l[j]
                swap = True
        if not swap:
            break
    out = []
    for i in l:
        out.append(i[1])
    return out

def findAlphabet(text):
    for i in text:
        if ord('a') <= ord(i) <= ord('z'):
            return i
    return None

inp = input('Enter Input : ').split()
out = sortAlphabet(inp)
for i in out:
    print(i, end=' ')