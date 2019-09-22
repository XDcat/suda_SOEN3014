# -*- coding:utf-8 -*-
'''
__author__ = 'XD'
__mtime__ = 2019/9/18
__project__ = 工业实践课程
Fix the Problem, Not the Blame.
'''


def bi_sum(x, y):
    """
    传入二进制字符串计算和
    :param x: 二进制字符串
    :param y: 二进制字符串
    :return: 和
    """
    x2 = int(x, 2)
    y2 = int(y, 2)
    return bin(x2 + y2)


def bi_muil(x, y):
    x2 = int(x, 2)
    y2 = int(y, 2)
    return bin(x2 * y2)


if __name__ == '__main__':
    print("二进制加法：")
    x = input("x = ")
    y = input("y = ")
    print("x + y = ", bi_sum(x, y))

    print("二进制乘法：")
    x = input("x = ")
    y = input("y = ")
    print("x * y = ", bi_muil(x, y))