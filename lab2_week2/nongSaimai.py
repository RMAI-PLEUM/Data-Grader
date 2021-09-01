# hbd(65) = "saimai is just 21, in base 32!"

# hdb(21) = "saimai is just 21, in base 10!"

# hdb(8888) = "saimai is just 20, in base 4444!"

def hbd(age):

    if (age%2==0):
        return "saimai is just 20, in base {}!".format(int(age/2))
    else:
        return "saimai is just 21, in base {}!".format(int(age//2))

year = input("Enter year : ")

print(hbd(int(year)))