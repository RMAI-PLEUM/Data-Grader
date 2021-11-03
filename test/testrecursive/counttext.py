def length(inp):
    check = 0
    def count(check, inp):
        if len(inp) == 0:
            print()
            print(check)
            return 
        if check%2 == 0:
            print(inp[0], end='*')
        if check%2 == 1:
            print(inp[0], end='+')
        check += 1
        inp = inp[1:]
        return count(check, inp)
    return count(check, inp)


inp = input('Enter Input : ')
length(inp)