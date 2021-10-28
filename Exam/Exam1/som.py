# inp = input("Enter :").split(" ")
# print(type(inp))
# print(inp)
# x,y,z = list(map(int,inp))
# print(x,y,z)

# Set = {'a','e','t'}
# dic = {'a':1,'b':2}
# print(dic['a'])

# class student:
#     def __init__(self):
#         pass
#     def addname(self, name, surname):
#         self.name = name
#         self.surname = surname
#     def display(self):
#         print("name is {}  surname is {}".format(self.name, self.surname))
    
# name = input("Enter your name: ").split()

# n1 = student()
# n1.addname(name[0], name[1])
# n1.display()

def trip(*args):
     print(args)
     print(args[:3])
     print(args[2])

# x = input("Enter data: ").split()
# trip(1,2,3,4,5)
print(91/2)
print(91//2) #หารปัดเศษลง

print("{:.2f}".format(23.342))

num = [2,56,3,57,5,8,100,4]
num.sort()
print(num)
num.reverse()
print(num)
print(num[0:2])