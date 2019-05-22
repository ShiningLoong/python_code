
def select_sort(lst):
    for i in range(len(lst)-1):
        key = i
        for j in range(i+1, len(lst)):
            if lst[i] < lst[j]:
                key = j
        tmp = lst[key]
        lst[key] = lst[i]
        lst[i] = tmp
    

        
