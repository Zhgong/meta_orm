db = [{"username": "yoshi", "age": 20}, {"username": "chunli", "age": 23}]


class Field:
    pass


class ModelMetaClass(type):
    def __new__(cls, name, bases, attrs):
        print(f"__new__ of {name}")
        if name == "Model":
            return ModelMetaClass.__class__.__new__(cls, name, bases, attrs)
        else:
            # print(attrs)
            fields = [k for k, v in attrs.items() if isinstance(v, Field)]
            # print(fields)
            def __init__(self, **kwargs):
                for k, v in kwargs.items():
                    if k in fields:
                        setattr(self, k, v)
                    else:
                        raise KeyError(f'Undefined field: "{k}"')

            attrs.update({"__init__": __init__})
            return ModelMetaClass.__class__.__new__(cls, name, bases, attrs)


class Model(metaclass=ModelMetaClass):
    @classmethod
    def query(cls, **kwargs):
        return [{"username": "yoshi", "age": 20}]


class User(Model):
    __tablename__ = "users"
    username = Field()

    def query(self):
        print("dummy")


customer = User(username="Zhou")
# customer = User()
print(customer.__dict__)


# user = User.query.filter_by(username=name).first()
