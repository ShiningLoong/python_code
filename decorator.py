def add_log1(f):     #单层decorator
    def wrapper(*args,**kw):
        print("a log1") 
        return f(*args,**kw)
    return wrapper			

#单层decorator调用方式 
#---@add_log1
#---def func1
#when execute func1,it is equal to add_log1(func1)(*args,**kw)
@add_log1	
def func1(x,y):
    return x*y

print(func1(22,33))


#2层decorator调用方式 
#---@add_log2(params)
#---def func2
#when execute func2,it is equal to add_log2(params)(func2)(*args,**kw)

def add_log2(param):
    print("log data is %s" % param) #do sth with param
    def wrapper1(f):
        pass
        def wrapper2(*args,**kw):
            pass
            return f(*args,**kw)
        return wrapper2
    return wrapper1
    
@add_log2(12345)
def func2(x,y):
    return x**y
    
print(func2(2,20))