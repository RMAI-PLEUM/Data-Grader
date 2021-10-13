
print("*** Rabbit & Turtle ***")
data = input("Enter Input : ").split(" ")
d, vr, vt ,vf = list(map(int,data))
sum = vf*(d/(vt-vr))
print("{:.2f}".format(sum))
