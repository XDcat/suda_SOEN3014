# -*- coding:utf-8 -*-
'''
__author__ = 'XD'
__mtime__ = 2019/9/19
__project__ = 工业实践课程
Fix the Problem, Not the Blame.
'''

import re
from time import time

start_time = time()
# sys.setrecursionlimit(1000000) # 设置递归深度为 1000000
# 读取字典和段落

with open(r"D:\Box\Pycharm_Project\工业实践课程\中文最大分词\data\corpus.dict.txt", encoding="utf-8") as f:
    dict = f.read()
with open(r"D:\Box\Pycharm_Project\工业实践课程\中文最大分词\data\corpus.sentence.txt", encoding="utf-8") as f:
    sentence = f.read()
with open(r"D:\Box\Pycharm_Project\工业实践课程\中文最大分词\data\corpus.answer.txt", encoding="utf-8") as f:
    sentence_given = f.read()


def split_word(index, length, maybe_dict):
    """使用迭代进行分词"""
    global sentence
    if index + length >= len(sentence):
        return index + length
    word = sentence[index: index + length]
    maybe_dict_new = "/n".join(re.findall(word + ".*", maybe_dict))  # 可能匹配的单词
    if maybe_dict_new:
        # 如果还有匹配的词汇，说明可以继续尝试匹配
        return split_word(index, length + 1, maybe_dict_new)
    else:
        # 如果没有匹配的词汇了，说明上一次匹配的值是最大的词汇
        sentence = sentence[: index + length - 1] + " " + sentence[index + length - 1:]
        return index + length


# 分词
index_real = 0
while len(sentence) != index_real:
    index_real = split_word(index_real, 1, dict)
# 寻找正确的个数
sentence_split_given = sentence_given.split()
sentence_split = sentence.split()

# sentence_split_given = sentence_given.split()[: 100]
# sentence_split = sentence.split()[: 100]

print("sentence_split_given_len:")
sentence_split_given_len = [0, ]
for i, j in enumerate(sentence_split_given):
    sentence_split_given_len.append(sentence_split_given_len[i] + len(j))
print(sentence_split_given_len)

print("sentence_split_len:")
sentence_split_len = [0, ]
for i, j in enumerate(sentence_split):
    sentence_split_len.append(sentence_split_len[i] + len(j))
print(sentence_split_len)

count = 0
index_given = 0  # sentence_split_given 的索引
sum_res = 0
sum_given = 0

for index_res in range(len(sentence_split)):
    # print(sum_res, "", end="")
    # 得到当前索引的 sum_res 和 下一个
    sum_next_res = sum_res + len(sentence_split[index_res])

    while sum_given < sum_res:
        sum_given += len(sentence_split_given[index_given])
        index_given += 1
        # print(sum_given, "", end="")

    # 比较当前和
    if sum_res == sum_given:
        # 如果当前和相等，比较下一个情况的和
        sum_given += len(sentence_split_given[index_given])
        index_given += 1
        # print(sum_given, "", end="")
        if sum_next_res == sum_given:
            count += 1
            # print("res = (%s, %s), given = (%s, %s)" % (
            # sum_res, sum_next_res, sum_given - len(sentence_split_given[index_given - 1]), sum_given))
    # else:
    #     print(sentence_split[index_res])
    #     print(sentence_split_given[index_given])
    sum_res = sum_next_res

len_sentence_split = len(sentence_split)
len_sentence_split_given = len(sentence_split_given)
print("自己找到的词数：", len_sentence_split)
print("参考找到的词数：", len_sentence_split_given)
print("匹配的数目：", count)
# 正确率(Precision) = 1 / 2 = 50.00 %
# 召回率(Recall) = 1 / 3 = 33.33 %
# F值 = (1 / 2) * (1 / 3) * 2 / (1 / 2 + 1 / 3) = 40.00 %
pricision = count / len_sentence_split
recall = count / len_sentence_split_given
print("正确率(Precision) = {} / {} = {:.2%}".format(count, len_sentence_split, pricision))
print("召回率(Recall) = {} / {} = {:.2%}".format(count, len_sentence_split_given, recall))
print("正确率(Precision) = {:.2%}".format(pricision * recall * 2 / (pricision + recall)))

end_time = time()
print("运行时间：",  end_time - start_time)