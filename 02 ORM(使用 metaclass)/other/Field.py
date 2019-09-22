# -*- coding:utf-8 -*-
'''
__author__ = 'XD'
__mtime__ = 2019/9/22
__project__ = 工业实践课程
Fix the Problem, Not the Blame.
'''

class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return "<%s:%s>" % (self.__class__.__name__, self.name)

class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, "String")


class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, "Int")