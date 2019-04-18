import logging
logging.basicConfig(level="DEBUG")
# set is a structure with no duplicated elements and not in any particular order

a = {1,2,3,4, 5, 5}
print(a)
# a[1]  # TypeError: 'set' object does not support indexing


# how to use enum
# use enumerates in for loop,we can easily get a counter in loop

for i, item in enumerate("abcdefg"):
    print(i, item)

a = enumerate("abcdefgh",2)
print(enumerate("abcdefgh"))
print(list(a))

print("_____________________________________________")
# list/ dic / set generator

lst = [x for x in range(10) if x % 2 == 0]

my_set = {x for x in "biabdvaibvasalnalsvHJAJKF" if x.islower()}

my_dic = {k : v for v in "1234567" for k in "ABCD"}   # how does this work
print(my_dic)
# in my_dic y is a fixed value of the last element in iterable
my_dic2 = {k : v for k in "1234567" for v in "ABCD"}
print(my_dic2)




my_list = [(k, v) for v in "1234567" for k in "ABCD"]

# print(my_list,'\n',my_set, '\n', my_dic)

logging.debug(len(my_list))

my_dic3 = dict()
for v in "1234567":
    for k in "ABCD":
        my_dic3[k] = v

print(my_dic3)


my_dic4 = dict()
for k in "1234567":
    for v in "ABCD":
        my_dic4[k] = v

print(my_dic4)