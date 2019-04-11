# 2nd time to write a simple ORM framework

# define the basic data structure

class Field:
    def __init__(self, name, content_type):
        self.name = name
        self.content_type = content_type

    def __str__(self):
        return '%s:%s' % (self.__class__.__name__, self.name)


class StringField(Field):
    def __init__(self, name):
        super().__init__(name, 'varcha[100]')

class IntField(Field):
    def __init__(self, name):
        super().__init__(name, 'Bigint')

class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):  # cls 是什么参数:需要创建的instance的class
        print('__new__ executed!!')  # 每次用metaclass定义一个新的class 都会执行__new__
        print('cls is:%s' % cls)
        print('name is %s' % name)
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print("Found model: %s" % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping:%s --> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
                attrs.pop(k)
        attrs['__mappings__'] = mappings
        attrs['__table__'] = name
        return type.__new__(cls, name, bases, attrs)

class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super().__init__(**kw)

    # def __getattr__(self, item):
    #     try:
    #         return self[item]
    #     except AttributeError:
    #         raise KeyError("'Model' has no attribute %s" % item)

    # def __setattr__(self, k, v):
    #     self[k] = v

    def save(self):
        columns = []
        values = []
        for k in self.__mappings__.keys():
            columns.append(k)
            values.append(str(self[k]))
        sql = "insert into %s (%s) values (%s)" % (self.__table__, ','.join(columns), ','.join(values))
        print("SQL: %s" % sql)


# testing code
class User(Model):
    name = StringField('name')
    id = IntField("id")
    gender = StringField("gender")
    money = IntField('money')

class test(Model):
    pass

class test2(test):
    pass


u = User(name="SpongeBob", id=12345, gender='Non', money=999999)
# u1 = User(name="SpongeBob", id=12345, gender='Non', money=999999)
# u2 = User(name="SpongeBob", id=12345, gender='Non', money=999999)
# u3 = User(name="SpongeBob", id=12345, gender='Non', money=999999)

# u.save()

print(type(Model))
print(type(User))
print(type(test))
print(type(test2))
print(type(u))
# Conclusions：
# 1. 对于含有metaclass 的 class, 用type查看均显示为  <class '__main__.NameOfMetaClass'>
# 2. 对于不含metaclass 的 class,用type查看均为 <class 'type'>
# 3. 当一个class 定义时包含了metaclass, 这个class就相当于metaclass的instance, 定义过程中会调用到metaclass的__new__方法

print('_________________________________________________')

# test __new__ without metaclass

class Test:
    def __new__(cls, a, b):
        print("__new__ executed!!")
        return super().__new__(cls, a, b)

    def __init__(self, a, b):
        self.a = a
        self.b = b


t = Test(1, 2)
t2 = Test(1, 2)
t3 = Test(1, 2)
