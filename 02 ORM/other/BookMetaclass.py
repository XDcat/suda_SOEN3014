# -*- coding:utf-8 -*-
'''
__author__ = 'XD'
__mtime__ = 2019/9/22
__project__ = 工业实践课程
Fix the Problem, Not the Blame.
'''
from other.Field import Field
from pprint import pprint

class BookMetaclass(type):
    def __new__(cls, name, bases, attrs):
        # # 如果是基类，则不做修改
        # if name == "Book":
        #     return type.__new__(cls, name, bases, attrs)

        pprint(attrs)
        # 针对属性，建立键值对映射
        mapping = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):  # 对是否是属性进行判断
                mapping[k] = v

        for k in mapping.keys():
            attrs.pop(k)

        attrs["__mappings__"] = mapping
        return type.__new__(cls, name, bases, attrs)
