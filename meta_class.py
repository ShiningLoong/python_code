#test python meta class
#with type() method we can create a class

ahello = type("hello", (object,), {}) #what dose the 1st arg use for?
a = ahello()
print(type(a)) #<class '__main__.hello'>

#the actual name of the class is 'hello' rather than 'ahello',
#but we should use "ahello" to create an instance, 'hello' is undefined

class hello2():
    pass
a2 = hello2()
print(type(a2))#<class '__main__.hello2'>


print('_____________________________分割线_______________________')

# class is an instance of metaclass

