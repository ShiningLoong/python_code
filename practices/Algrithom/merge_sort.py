# coding: utf8
from random import random

def merge(l, h, i ,t):
    list_A = l[h:i+1] + [float('inf')]
    list_B = l[i+1:t+1] + [float('inf')]
    key_A, key_B = 0,0
    for k in range(h, t+1):
        if list_A[key_A] < list_B[key_B]:
            l[k] = list_A[key_A]
            key_A += 1
        else:
            l[k] = list_B[key_B]
            key_B += 1

            

def merge_sort(lst, head, tail):
    if head == tail:
        return
    intv = (tail+ head) // 2
    merge_sort(lst, head, intv)
    merge_sort(lst, intv+1, tail)
    merge(lst, head, intv, tail)

if __name__ == "__main__":
    l = [round(random()*1000)for x in range(30)]
    merge_sort(l, 0, 29)
    print(l)
