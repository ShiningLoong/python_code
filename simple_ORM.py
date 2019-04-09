# write a simple ORM framework
# construct SQL sentence as below:
# SQL: insert into User (id,email,username,password) values (?,?,?,?)
# ARGS:[12345, 'test@orm.org', 'Michael', 'my-pwd']
# 1.basic data structure of object to describe a database
class Field(dict):
    def __init__(self, name, column_type):
        super.__init__()
        self.name = name
        self.name = self.name
        self.column_type = column_type

# 2.different kind of content type based on Field
class IntField(Field):
    def __init__(self, name):
        super().__init__(name, 'bigint')

class StringField(Field):
    def __init__(self, name):  # 这里并没有提示self未被使用
        super().__init__(name, 'varchar[100]')  # in old version of python, self should be passed to super()

class ModelMetaclass(type):
    pass

class Model(metaclass=ModelMetaclass):
    pass

