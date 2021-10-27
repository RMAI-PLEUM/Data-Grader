    index = int(buffer[0])
    data = int(buffer[1])
    
    if index >= 0 and index <= len((l)):
            l.insertAfter(index, data)
            print(f'index = {index} and data = {data}')
    else:
            print('Data cannot be added')
if (l.isEmpty()):
    print('List is empty')
else:
    print(f'link list : {l}')