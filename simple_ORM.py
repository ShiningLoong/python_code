# write a simple ORM framework
# construct SQL sentence as below:
# SQL: insert into User (id,email,username,password) values (?,?,?,?)
# ARGS:[12345, 'test@orm.org', 'Michael', 'my-pwd']
# 1.basic data structure of object to describe a database
class Field:
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '%s:%s' % (self.__class__.__name__, self.name)

# 2.different kind of content type based on Field
class IntField(Field):
    def __init__(self, name):
        super().__init__(name, 'bigint')

class StringField(Field):
    def __init__(self, name):  # 这里并没有提示self未被使用
        super().__init__(name, 'varchar[100]')  # in old version of python, self should be passed to super()

class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print("Found model %s" % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print("Found mapping %s --> %s" % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings
        attrs['__table__'] = name
        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError("'Model' object has no attribute '%s'" % key)

    # def __setattr__(self, key, value):
    #     self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
            # args.append(str(self[k]))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % args)

# test code
class User(Model):
    id = IntField('id')
    name = StringField('name')
    gender = StringField('gender')

#
# u = User(id=12345, name='Sponge', gender='male')
# u.save()