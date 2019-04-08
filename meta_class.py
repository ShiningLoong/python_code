# test python meta class
# with type() method we can create a class

ahello = type("hello", (object,), {})  # what dose the 1st arg use for?
a = ahello()
print(type(a))  # <class '__main__.hello'>

# the actual name of the class is 'hello' rather than 'ahello',
# but we should use "ahello" to create an instance, 'hello' is undefined


class Hello2:
    pass


a2 = Hello2()
print(type(a2))  # <class '__main__.hello2'>


print('_____________________________分割线_______________________')
# class is an instance of metaclass

# write a meta class and use it

class ListMetaclass(type):  # object是type的 instance , object 也是type 的 父类
    def __new__(mcs, name, bases, attrs):
        # __new__供系统调用用于创建一个class,class本身也是一个instance
        # mcs 参数可以理解为指向要创建的instance的指针（暂时这么认为），这个instance就是我们要创建的class
        attrs["add"] = lambda self, value: self.append(value)
        return type.__new__(mcs, name, bases, attrs)


class MyList(list, metaclass=ListMetaclass):
    def __init__(self, **kw):
        super(MyList, self).__init__(**kw) # 用.下标执行__init__函数时实际上已经传递了第一个参数self


mylist = MyList()
mylist.add(123)

print('_____________________________分割线_______________________')

# write a object relational mapping (ORM) Framework

class Field:
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)

class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, "varchar[100]")

class IntField(Field):
    def __init__(self, name):
        super(IntField, self).__init__(name, "bigint")

class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == "Model":
            return type.__new__(cls, name, bases, attrs)
        print("Found Model:%s" % name)
        mappings = dict()
        print(attrs.items())
        for k, v in attrs.items():
            if isinstance(v, Field):
                print("Found mapping:%s->%s" % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs["__mappings__"] = mappings
        attrs["__table__"] = name
        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError("'Model' object has no attribute '%s'"% key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append("?")
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print("ARGS:%s" % str(args))
# definition end
# how to use ORM↓

class User(Model):
    id = IntField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')


u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# u = User()
u.save()

# m = Model(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# m.save()
print('_____________________________分割线_______________________')

# test how dict initializing
class MyDict(dict):
    pass
    para1 = StringField("para1")
    para2 = IntField("para2")  # In this case , para1 and para2 are 2 attributes of MyDict.


mydict = MyDict(para1='1', para2='2')  # In this case, para1 and para2 are key-values (NOT attributes) of mydict
print(type(mydict.para1))  # still don't know how key-values are stored in a dict,need to check CPython source code
print(type(mydict.para2))
print(mydict.keys())
print(mydict.values())
print("%s" % mydict.para1)

# mydict2 = MyDict()
# print(mydict2)
# print(dir(mydict))

# Summary:
