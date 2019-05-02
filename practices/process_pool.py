class ModelMetaClass(type):
    def __new__(cls, name, base, attrs):
        mapping = dict()
        attrs["__table__"] = name
        for k, v in attrs.items():
            if isinstance(v, Field):
                mapping[k] = v
        for
        return type.__new__(cls, name, base, attrs)


class Field:
    def __init__(self, column_name, column_type):
        self.name = column_name
        self.type = column_type


class IntField(Field):
    def __init__(self, name):
        super().__init__(name, "BigInt")


class StrField(Field):
    def __init__(self, name):
        super().__init__(name, "varchar100")


class Model(dict, metaclass=ModelMetaClass):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError("attribute %s does not exist" % item)


class StudentModel(Model):
    name = StrField("name")
    age = IntField("age")
    gender = StrField("gender")






