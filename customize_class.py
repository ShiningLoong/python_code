#define a fibonacci class , and use it as a iterator
#use enumerate
from enum import Enum
from collections import Iterable,Iterator
Gender = Enum('gender',('female','male'))

class Student():# without  __next__ method
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender
    
    def __iter__(self):
        pass
        # return [1,2,3].__iter__()

    def __next__(self):
        pass
# for a in Student('Tom', Gender.male):
    # print(a)
 
a = Student('Tom',Gender.male)
print(isinstance(a,Iterable))
print(isinstance(a,Iterator))
next(a)
print('_________________分割线_____________________')
#results: 
# if class A has __iter__ method , A is iterable;
# on the basis of that, if __iter__ returns a iterator , A can be used in 'for' statements 
# if A has both __iter__ and __next__ , A is a Iterator

class Fib():
    def __init__(self, stop):
        self.a = 0
        self.b = 1
        self.stop = stop
#if want to get fib[n] by index n,use  __getitem__ method
    def __iter__(self):
        return self
        
    def __next__(self):
        self.a , self.b = self.b, self.a + self.b
        if self.a < self.stop :
            return self.a
        else:
            raise StopIteration
            
    def __getitem__(self,n):
        a ,b = 0, 1
        for i in range(n):
            a, b = b, a+b
        return a
        

fib = Fib(1000)

for n in fib:
    print(n)

for n in range(10):
    print('the %s item of fib is %s'% (n, fib[n]) )   
    
print('_________________分割线_____________________')



#how to use __getattr__

class AStudent():
    pass
    
astudent = AStudent()
# astudent.name
#AttributeError ,it doesn't have 'name' attr

class BStudent():
    def __getattr__(self,arg):
        pass
        
bstudent = BStudent()
print(bstudent.name)     #call bstudent.__getattr__(self,'name') and it returns default value:  None
print('_________________分割线_____________________')


# chain call
class Chain():
    def __init__(self,path = ''):
        self.path = path
        
    def __getattr__(self,para):
        if para == 'user' :
            return Chain(self.path)
        return Chain(self.path + '/' + para)
#call a class' instance directly by __call__
    def __call__(self,para):
        return Chain(self.path + '/' + para)
chain = Chain('home')        
print(chain.get.name.what.path)
print(chain.user('tom').dosth.done.path)




