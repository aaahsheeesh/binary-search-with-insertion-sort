def sort( values ):
    n = len(values) # size of list
    for i in range(n - 1):
        for j in range(n - i - 1):
    	```move the smallest digit to the front, one step at a time```
            if values[j] > values[j + 1]:
                # swapping
                temp = values[j]
                values[j] = values[j + 1]
                values[j + 1] = temp
    return values
