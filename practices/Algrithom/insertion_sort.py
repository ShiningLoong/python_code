def insert_sort(lst):
    for i in range(1,len(lst)):
        tmp = lst[i]
        j = i-1
        while j >= 0 and tmp > lst[j]:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = tmp
