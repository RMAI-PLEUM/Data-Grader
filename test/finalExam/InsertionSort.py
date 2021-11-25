def insert_sort(lst, simulation = False):
    for i in range(len(lst)):
        cursor = lst[i]
        pos = i

        while pos > 0 and lst[pos - 1] > cursor:
            #swap number down the list
            lst[pos] = lst[pos-1]
            pos = pos - 1
        #break and do the final swap
        lst[pos] = cursor
    return lst
