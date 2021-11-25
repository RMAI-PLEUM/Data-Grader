def Sort_ignor_negative(list):
    for i in range(len(list)):
        if list[i] < 0:
            continue
        min = [-1,1]
        for j in range(i, len(list)):
            if list[j] < 0:
                continue
            if min[1] > list[j]:
                min[0] = j
                min[1] = list[j]
    
        list[i], list[min[0]] = list[min[0]], list[i]
    return list

inp = list(map(int,input('Enter Input : ').split()))
for i in Sort_ignor_negative(inp):
    print(f'{i}', end=' ')
