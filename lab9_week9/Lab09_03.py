maxtomin = False
mintomax = False
samenum = False

def somethingDrome(list):
    global maxtomin
    global mintomax
    global samenum

    if list[0] > list[1]:
        for i in range(len(list)-1):
            if list[i] > list[i+1]:
                maxtomin = True
            if list[i] == list[i+1]:
                samenum = True
            if list[i] < list[i+1]:
                mintomax = True
        
    
    elif list[0] < list[1]:
        for i in range(len(list)-1):
            if list[i] > list[i+1]:
                maxtomin = True
            if list[i] == list[i+1]:
                samenum = True
            if list[i] < list[i+1]:
                mintomax = True
        
    
    elif list[0] == list[1]:
        for i in range(len(list)-1):
            if list[i] > list[i+1]:
                maxtomin = True
            if list[i] == list[i+1]:
                samenum = True
            if list[i] < list[i+1]:
                mintomax = True
    
    if mintomax == True and samenum == False and maxtomin == False :
        print('Metadrome')
    elif mintomax == True and samenum == True and maxtomin == False :
        print('Plaindrome')
    elif mintomax == False and samenum == False and maxtomin == True :
        print('Katadrome')
    elif mintomax == False and samenum == True and maxtomin == True :
        print('Nialpdrome')
    elif mintomax == False and samenum == True and maxtomin == False :
        print('Repdrome')
    else :
        print('Nondrome')


inp = list(map(int, ''.join(input('Enter Input : '))))
somethingDrome(inp)
