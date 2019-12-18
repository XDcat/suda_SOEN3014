# -*- coding:utf-8 -*-
'''
__author__ = 'XD'
__mtime__ = 2019/10/10
__project__ = 工业实践课程
Fix the Problem, Not the Blame.
'''
import configparser
import os
import re
import uuid
import logging

# 设置 logging 格式
# logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.DEBUG, format='%(module)s - fnc: %(funcName)s() - line: %(lineno)d - %(levelname)s - %(message)s')
class Book():
    """所有 Book 的父类
    不同的类保存在不同的文件中，文件的路径根据配置当前路径的配置文件。
    """

    def __init__(self):
        # 设置日志对象
        self.id = None # 主键：1. 在插入时递增最大值 2. 查询时赋值
        self.file_basepath = self.get_file_basepath()  # 文件保存的目录
        self.file_path = "%s%s.txt" % (self.get_file_basepath(), self.__class__.__name__)
        if not os.path.isfile(self.file_path):
            open(self.file_path, "w", encoding="utf-8").close()  # 如果文件不存在则创建
    def add(self):
        """
        增
        1. 如果在文件中，则无法插入
        2. 如果不在文件中，则插入
        """
        if self.is_in_file():
            logging.info("插入对象失败：文件中已经存在此对象")
            return

        # 查询 id 的最大值
        max_id = 0
        with open(self.file_path, encoding="utf-8") as f:
            lines = f.readlines()
            # 只有在文件中有数据时，查询
            if lines:
                last_line = lines[-1]
                max_id = int(last_line.split(",")[0])

        self.id = max_id + 1  # 为 id 赋值
        with open(self.file_path, "a", encoding="utf-8") as f:
            f.write(self.__str__(True) + '\n')
        logging.info("插入对象:%s" % self.__str__())

    def save(self):
        """
        改
        1. 如果在文件中，则更新
        2. 如果不在文件中，则提示无法更新
        """
        if self.is_in_file():
            # 如果存在记录，更新
            with open(self.file_path, encoding="utf-8") as f:
                text = f.read()
            with open(self.file_path, "w", encoding="utf-8") as f:
                text = re.sub("%s,.*" % self.id, self.__str__(True), text)
                f.write(text)
            logging.info("更新 id = %s 的记录" % self.id)
        else:
            logging.info("无法更新: 文件中没有 id = %s 的记录" % self.id)
    def destroy(self):
        """
        删
        1. 如果文件中不存在，则提示
        2. 如果文件中存在，则删除
        """
        if self.is_in_file():
            #  如果在文件中，删除
            with open(self.file_path, encoding="utf-8") as f:
                text = f.read()
            with open(self.file_path, "w", encoding="utf-8") as f:
                text = re.sub("%s,.*?\n" % self.id, "", text)
                f.write(text)
            logging.info("删除对象:" + self.__str__())
        else:
            # 如果不存在，提示
            logging.info("正在删除不存在对象:" + self.__str__())


    @classmethod
    def find(cls, id):
        """
        查 （根据 id 查询）
        1. 如果文件中不存在，返回 None
        2. 如果文件中存在，则 返回对象
        """
        # 如果 id 还没有赋值，可以直接判断不存在
        if id == None:
            return None
        # 获取当前类的所有子类
        sub_cls_list = Book.__all_subcls()
        attr_v = None  # 寻找的对象的属性
        for sub_cls in sub_cls_list:  # 每一个 sub_cls 都是一个类，可以直接实例化
            sub_cls_name = sub_cls.__name__  # 获取类命
            if not os.path.isfile("%s%s.txt" % (Book.get_file_basepath(), sub_cls_name)):
                # 如果文件不存在则跳过
                continue
            with open("%s%s.txt" % (Book.get_file_basepath(), sub_cls_name), encoding="utf-8") as f:
                attr_v = re.search("%s,.*" % id, f.read())  # 属性值
                if attr_v:
                    attr_v = attr_v.group().split(",")[1:]
                    # 如果不为空就是找到了
                    # 找到后，实例化对象
                    book = sub_cls()
                    attr_k = list(book.get_all_attr().keys())
                    if len(attr_k) != len(attr_v):
                        # 如果数量不一致，说明数据已经发生了变动，无法映射
                        raise RuntimeError("%s 属性以及发生改变，无法映射")
                    for i in range(len(attr_v)):
                        setattr(book, attr_k[i], attr_v[i])
                    logging.info("找到 id = %s 的对象: %s" % (id, book.__str__()))
                    return book
        logging.info("并没有找到 id = %s 的记录" % id)
        return None




    def get_all_attr(self):
        """获取对象所有属性"""
        all_attr = {}
        for i in dir(self):
            # 排除一些魔术方法
            if i in ["__module__", "id"]:
                continue

            # 排除配置文件中要求的不需要的属性
            if os.path.isfile("./config.ini"):
                config = configparser.ConfigParser()
                config.read("./config.ini")
                try:
                    ignore_attr = config.get("file", "ignore")
                    if i in ignore_attr.split(","):
                        continue
                except configparser.NoOptionError:
                    logging.info("配置文件中并不存在 file.ignore")

            # 添加属性
            if isinstance(getattr(self, i), (int, float, str, )):
                all_attr[i] = str(getattr(self, i))
        return all_attr

    def is_in_file(self):
        """判断对象是否以及保存在文件中"""
        return bool(self.find(self.id))

    @classmethod
    def get_file_basepath(cls):
        """获取文件保存的 basepath"""
        # 判断配置文件是否存在
        if os.path.isfile("./config.ini"):
            # 在配置文件中读取 basepath
            config = configparser.ConfigParser()
            config.read("./config.ini")
            try:
                basepath = config.get("file", "basepath")
            except configparser.NoOptionError:
                logging.warning("配置文件中不存在 basepath，写入配置文件并返回默认路径")
                basepath = "./data/"
                # 写入配置文件
                config.set("file", "basepath", basepath)
                with open(r"./config.ini", "w", encoding="utf-8") as f:
                    config.write(f)

        else:
            # 不存在配置文件，创建配置文件，并返回默认路径
            logging.warning("当前路径不存在配置文件，创建默认配置文件，并返回默认路径")
            with open(r"./config.ini", "w", encoding="utf-8") as f:
                f.write("[file]\nbasepath = ./data/")
            basepath = "./data/"
        return basepath

    def __str__(self, flag=False):
        """
        flag = True: 只返回属性；
        flag = Flase: 类名，所有属性
        """
        attr = str(self.id) + "," + ','.join(list(self.get_all_attr().values()))  # 所有属性
        if flag:
            return attr
        else:
            return self.__class__.__name__ + "," + attr
    @classmethod
    def __all_subcls(cls):
        """获得当前类的所有子类，包括子类的子类"""
        # 使用递归求
        def get_all_sub_cls(parent_cls):
            sub_cls = [parent_cls, ]
            for i in parent_cls.__subclasses__():
                sub_cls += get_all_sub_cls(i)
            return sub_cls
        return get_all_sub_cls(Book)


class ComputerBook(Book):
    def __init__(self, name="", star="", author="", public=""):
        """
        有关计算机的书
        :param name: 书名
        :param star: 评分
        :param author: 作者
        :param public: 出版社
        """
        super().__init__()
        self.name = name
        self.star = star
        self.author = author
        self.public = public
class LinuxBook(ComputerBook):
    def __init__(self, name="", star="", author="", public=""):
        super().__init__(name, star, author, public)
        self.des = "有关于 Linux 的书籍"

class DatabaseBook(ComputerBook):
    def __init__(self, name="", star="", author="", public="", kind=""):
        super().__init__(name, star, author, public)
        self.kind = kind
if __name__ == '__main__':
    linux_book = LinuxBook("UNIX环境高级编程", "9.5", "Stephen A. Rago", "人民邮电出版社")
    logging.debug("创建 LinuxBook 对象：%s" % linux_book)
    logging.debug("没有插入，更新对象")
    linux_book.save()
    logging.debug("没有插入，插入对象")
    linux_book.add()
    logging.debug("插入后，更新对象")
    linux_book.save()
    logging.debug("插入后，删除对象")
    linux_book.destroy()
    logging.debug("没有插入，使用类查找对象")
    logging.debug(Book.find(linux_book.id))
    logging.debug("没有插入，使用对象查找对象")
    logging.debug(linux_book.find(linux_book.id))
    logging.debug("插入后，使用类查找对象")
    linux_book.add()
    logging.debug(Book.find(linux_book.id))
    logging.debug("插入后，使用对象查找对象")
    logging.debug(linux_book.find(linux_book.id))
