#!/usr/bin/python3
# -*- coding:utf-8 -*-


class Field(object):

    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)


class StringField(Field):

    def __init__(self, name, length):
        super(StringField, self).__init__(name, f'varchar({length})')


class IntegerField(Field):

    def __init__(self, name):
        assert isinstance(name, int), "传入类型错误"
        super(IntegerField, self).__init__(name, 'int')


class CharField(Field):

    def __init__(self, name, length):
        super(CharField, self).__init__(name, f'char({length})')


class TextField(Field):

    def __init__(self, name):
        super(TextField, self).__init__(name, 'text')


class DateField(Field):

    def __init__(self, name):
        super(DateField, self).__init__(name, 'date')


class ModelMetaclass(type):

    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings # 保存属性和列的映射关系
        attrs['__table__'] = name # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))

    def db_query(self):
        pass

    def db_select(self):
        pass

    def db_update(self):
        pass

    def db_delete(self):
        pass

    def db_insert(self):
        pass


class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username', 50)
    email = StringField('email', 50)
    password = StringField('password', 50)


if __name__ == '__main__':
    u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
    u.save()
