def length(txt):     
    check = 0
    def count(check, text):
        if text == '':
            return 0
        if check%2 == 0:
            print(text[0], end='*')
        if check%2 == 1:
            print(text[0], end='~')
        check += 1
        text  = text[1:]
        return  1 + count(check, text)
            

    return count(check, txt)
print("\n",length(input("Enter Input : ")),sep="")
