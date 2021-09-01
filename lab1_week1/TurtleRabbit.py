
print("*** Rabbit & Turtle ***")
data = input("Enter Input : ").split(" ")
d, vr, vt ,vf = list(map(int,data))
S = vf*(d/(vt-vr))
print("{:.2f}".format(S))
# djf;sldhf