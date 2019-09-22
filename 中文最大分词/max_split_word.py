# -*- coding:utf-8 -*-
'''
__author__ = 'XD'
__mtime__ = 2019/9/19
__project__ = 工业实践课程
Fix the Problem, Not the Blame.
'''
# 读取字典和段落
import re

with open(r"D:\Box\Pycharm_Project\工业实践课程\中文最大分词\data\corpus.dict.txt", encoding="utf-8") as f:
    dict = f.read()
with open(r"D:\Box\Pycharm_Project\工业实践课程\中文最大分词\data\corpus.sentence.txt", encoding="utf-8") as f:
    sentence = f.read()
# sentence = sentence[: len(sentence) // 5]
sentence = "戴相龙说中国经济发展为亚洲作出积极贡献"

def iter_sentence(index):
    """
    遍历段落进行分词
    :param index: 索引
    :return:
    """
    global sentence
    global dict
    if len(sentence) > index:
        return split_word(index, 1, dict)


def split_word(index, length, maybe_dict):
    """使用迭代进行分词"""
    global sentence
    if index+length >= len(sentence):
        iter_sentence(index + length)
    word = sentence[index: index + length]
    maybe_dict_new = "/n".join(re.findall(word + ".*", maybe_dict))  # 可能匹配的单词
    if maybe_dict_new:
        # 如果还有匹配的词汇，说明可以继续尝试匹配
        return split_word(index, length + 1, maybe_dict_new)
    else:
        # 如果没有匹配的词汇了，说明上一次匹配的值是最大的词汇
        sentence = sentence[: index + length - 1] + " " + sentence[index + length - 1:]
        print(sentence)
        iter_sentence(index + length)

iter_sentence(0)
print(sentence)