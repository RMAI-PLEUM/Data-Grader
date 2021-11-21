def BubbleSort(list):
    count = 0
    for i in range(len(list)-1):
        swap = None
        has_swap = False
        for j in range(len(list)-i-1):
            if list[j] > list[j+1]:
                swap = list[j]
                list[j],list[j+1] = list[j+1],list[j]
             
                has_swap = True
        count += 1

        if has_swap is False or i == len(list)-2:
            print(f'last step : {list}', end=' ')
            print(f'move[{swap}]')
            return
        else:
            print(f'{count} step : {list}',end=' ')
            print(f'move[{swap}]')

inp = list(map(int,input('Enter Input : ').split()))
BubbleSort(inp)