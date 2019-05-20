    
def inst(l, k, v):
    return l[:k]+[v]+l[k:]


def inst_sort(lst):
    if len(lst) <= 1:
        return lst
    sorted_lst = list(lst[:1])
    for i in range(1, len(lst)):
        for j in range(i):
            if lst[i] <= lst[j]:
                sorted_lst = inst(sorted_lst, j, lst[i])
                break
            elif j == i-1:
                sorted_lst = inst(sorted_lst, j+1, lst[i])
    return sorted_lst

    
