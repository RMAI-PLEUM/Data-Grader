print("*** Election ***")
numvote = int(input("Enter a number of voter(s) : "))
vote = input("").split(" ")
candidate = []
bool = []
for i in range(1,21,1):
    candidate.append(i)

v = list(map(int,vote))

for i in range(0,len(v),1):
    bool.append(v[i] in candidate)

cart = []
i =1
while i<=20:
     # print("cout {} = {}".format(i,v.count(i)))
     cart.append(v.count(i))
     i+=1

# print(cart)
max = 0 
j = 0
while j<20:
        if(cart[j]>=max):
            max = cart[j]
        else:
            max = max
        j+=1

# print(max)
# print(cart.index(max))

# print(candidate)
if (True in bool):
    print(candidate[cart.index(max)])
else:
    print("*** No Candidate Wins ***")
