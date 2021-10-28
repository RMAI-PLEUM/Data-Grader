# def RomToInt(x):
#     roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}

#     index = 0
#     Int = 0
#     while(index < len(x)):
#         if x[index:index+2] in roman:
#             Int += roman[x[index:index+2]]
#             index += 2
#         else:
#             Int += roman[x[index]]
#             index += 1
#     return Int
        
# print(RomToInt("MMIX"))

dicnum = {1:"1",2:"2",3:'3',4:'5',6:'6',7:'7',8:'8',9:'9',10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
print(dicnum[10])

