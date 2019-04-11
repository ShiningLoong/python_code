# test how to use exceptions

a = 1
try:
    a/0
    print('This will not happen!')
except ZeroDivisionError:
    print('catched')

print('This will happen!')

class A:
    pass

class B(A):
    pass


a = A()
tup = (A, B)
print(isinstance(a, tup))

# By the way ,let's test the funcion tools

#return 2 values

def ret2(x,y):
    return x+1, y+1

a = ret2(1,2)
print(a)  # return  a tuple!

import functools
items = [[0,1], [0, 2], [0,3], [0,4], [0,5]]
total = functools.reduce(lambda a, b: (0, a[1] + b[1]), items)[1]
print(total)


# test log
import logging

try:
    1/0
except ZeroDivisionError as e:
    logging.exception(e)

print('catched!')
