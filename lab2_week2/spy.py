def bon(w):
    j = len(w)
    i = 0
    s = [0]
    while (i<j):
        if (w.count(w[i])>1):
            s[0] = w[i]
            break
        else:
            pass
        i+=1
    num = ord(s[0])-96
    return num*4
secretCode = input("Enter secret code : ")
print(bon(secretCode))

#หาตัวซ้ำ *4