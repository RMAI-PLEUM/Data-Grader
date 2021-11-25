same = False
maxtomin = False
mintomax = False

def somethingDrome(lst):
    global same
    global maxtomin
    global mintomax


    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            maxtomin = True
        elif lst[i] < lst[i+1]:
            mintomax = True
        elif lst[i] == lst[i+1]:
            same = True
    # print(f'same {same}')
    # print(f'maxtomin {maxtomin}')
    # print(f'mintomax {mintomax}')

    if mintomax == True and same == False and maxtomin == False :
        print('Metadrome')
    elif mintomax == True and same == True and maxtomin == False :
        print('Plaindrome')
    elif mintomax == False and same == False and maxtomin == True :
        print('Katadrome')
    elif mintomax == False and same == True and maxtomin == True :
        print('Nialpdrome')
    elif mintomax == False and same == True and maxtomin == False :
        print('Repdrome')
    else :
        print('Nondrome')


inp = list(map(int, ''.join(input('Enter Input : '))))

somethingDrome(inp)

