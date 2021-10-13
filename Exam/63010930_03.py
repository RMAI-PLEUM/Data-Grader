
a = "abcdefghijklmnopqrstuvwxyz"
b = a.upper()
lower = []
upper = []
for i in a:
    lower.append(i)
for i in b:
    upper.append(i)


print(" *** String count ***")
x = input("Enter message : ")
ch = ''
i = 0
while i < len(x):
    if x[i] in lower or x[i] in upper:
        ch += x[i]
    i+=1

i = 0
countUp = 0
countLow = 0
sUp = []
sLow = []
while i<len(ch):
    if ch[i] in upper:
        countUp += 1
        sUp.append(ch[i])
    else:
        countLow += 1
        sLow.append(ch[i])
    i += 1
ordUp = []
ordLow = []
for i in sUp:
    ordUp.append(int(ord(i)))
ordUp == ordUp.sort()
numUp = []

j = 0
while j < len(ordUp):
    if ordUp[j] in numUp:
        j+=1
        continue
    numUp.append(ordUp[j])
    j+=1
stUp = ''
for i in numUp:
    stUp += chr(i) + "  "

for i in sLow:
    ordLow.append(int(ord(i)))
ordLow == ordLow.sort()
numLow = []

j = 0
while j < len(ordLow):
    if ordLow[j] in numLow:
        j += 1
        continue
    numLow.append(ordLow[j])
    j+=1
stLow = ''
for i in numLow:
    stLow += chr(i) + "  "

print("No. of Upper case characters : {}".format(countUp))
print("Unique Upper case characters : {}".format(stUp))
print("No. of Lower case Characters : {}".format(countLow))
print("Unique Lower case characters : {}".format(stLow))

