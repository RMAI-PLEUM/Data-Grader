def Asteroid(x):
    if len(x) <= 1:
        return x
    list = Asteroid(x[1:])
    if len(list) is not 0 and x[0] > 0 and list[0] < 0:
        if x[0] > abs(list[0]):
            return Asteroid([x[0]] + list[1:])
        elif x[0] is abs(list[0]):
            if len(list) > 1:
                return list[1:]  
            else:
                return []
        else:
            return list
    else:
        return [x[0]] + list

x = input("Enter Input : ").split(",")
x = list(map(int,x))
print(Asteroid(x))