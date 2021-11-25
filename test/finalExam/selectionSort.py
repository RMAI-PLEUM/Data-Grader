def selection_sort(lst):
    for i in range(len(lst)):
        minimum = i

        for j in range(i + 1, len(lst)):
            #Select the smallest value
            if lst[j] < lst[minimum]:
                minimum = j
        #Place it at the front of the
        #sorted end of the list
        lst[minimum], lst[i] = lst[i], lst[minimum]
    
    return lst