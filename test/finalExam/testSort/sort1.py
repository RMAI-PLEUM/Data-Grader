def bubble_sort(lst):
    count = 0
    for i in range(len(lst)-1):
        
        swap = None
        swapped = False
        for j in range(len(lst)-i-1):
            if lst[j] > lst[j+1]:
                swap = lst[j]
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swapped = True
    
        count += 1
        if swapped == False or i == len(lst)-2:
            print(f'last step : {lst}', end=' ')
            print(f'move[{swap}]')
            return     
          
        else:
            print(f'{count} step : {lst}',end=' ')
            print(f'move[{swap}]')
        
               
l = [4,3,2,1]
bubble_sort(l)
