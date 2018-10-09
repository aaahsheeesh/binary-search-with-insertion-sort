def search( values, key ):
    values = sort(values) # sorted array to be fed into binary search
    n = len(values) # size
    start = 0
    end  = n - 1
    middle = (start + end)//2
    while start <= end:
        if values[middle] is key:
            print ("Found!")
            break
        elif values[middle] < key:
            start = middle + 1
        else:
            end = middle - 1
        middle = (start + end)//2
    else: # means there is nothing left to be searched in
        print ("Not found!")
