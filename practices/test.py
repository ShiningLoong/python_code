def func():
    lst = list()
    for x in range(3):
        def f():
            return x
        lst.append(f)
    return lst

f = func()
print(f[1].__closure__)