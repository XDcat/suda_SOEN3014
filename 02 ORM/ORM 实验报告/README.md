## 如何运行示例代码
```angular2
python ./Book.py
```

## 说明
1. data 文件夹，存放着数据存储文件以及存有一些样本数据 excel 文件
2. Book.py 文件
    1. Book 类，对数据进行操作，具体如下
        * 增：add()
        * 删：destroy()
        * 改：save()
        * 查：find()
    2. main 函数，使用 Book 类的一些例子
        ```angular2
       python ./Book.py
        ```
     3. 结果展示
         ```
        Book - fnc: <module>() - line: 228 - DEBUG - 创建 LinuxBook 对象：LinuxBook,None,Stephen A. Rago,有关于 Linux 的书籍,UNIX环境高级编程,人民邮电出版社,9.5
        Book - fnc: <module>() - line: 229 - DEBUG - 没有插入，更新对象
        Book - fnc: save() - line: 68 - INFO - 无法更新: 文件中没有 id = None 的记录
        Book - fnc: <module>() - line: 231 - DEBUG - 没有插入，插入对象
        Book - fnc: add() - line: 51 - INFO - 插入对象:LinuxBook,7,Stephen A. Rago,有关于 Linux 的书籍,UNIX环境高级编程,人民邮电出版社,9.5
        Book - fnc: <module>() - line: 233 - DEBUG - 插入后，更新对象
        Book - fnc: find() - line: 119 - INFO - 找到 id = 7 的对象: LinuxBook,None,Stephen A. Rago,有关于 Linux 的书籍,UNIX环境高级编程,人民邮电出版社,9.5
        Book - fnc: save() - line: 66 - INFO - 更新 id = 7 的记录
        Book - fnc: <module>() - line: 235 - DEBUG - 插入后，删除对象
        Book - fnc: find() - line: 119 - INFO - 找到 id = 7 的对象: LinuxBook,None,Stephen A. Rago,有关于 Linux 的书籍,UNIX环境高级编程,人民邮电出版社,9.5
        Book - fnc: destroy() - line: 82 - INFO - 删除对象:LinuxBook,7,Stephen A. Rago,有关于 Linux 的书籍,UNIX环境高级编程,人民邮电出版社,9.5
        Book - fnc: <module>() - line: 237 - DEBUG - 没有插入，使用类查找对象
        Book - fnc: find() - line: 121 - INFO - 并没有找到 id = 7 的记录
        Book - fnc: <module>() - line: 238 - DEBUG - None
        Book - fnc: <module>() - line: 239 - DEBUG - 没有插入，使用对象查找对象
        Book - fnc: find() - line: 121 - INFO - 并没有找到 id = 7 的记录
        Book - fnc: <module>() - line: 240 - DEBUG - None
        Book - fnc: <module>() - line: 241 - DEBUG - 插入后，使用类查找对象
        Book - fnc: find() - line: 121 - INFO - 并没有找到 id = 7 的记录
        Book - fnc: add() - line: 51 - INFO - 插入对象:LinuxBook,7,Stephen A. Rago,有关于 Linux 的书籍,UNIX环境高级编程,人民邮电出版社,9.5
        Book - fnc: find() - line: 119 - INFO - 找到 id = 7 的对象: LinuxBook,None,Stephen A. Rago,有关于 Linux 的书籍,UNIX环境高级编程,人民邮电出版社,9.5
        Book - fnc: <module>() - line: 243 - DEBUG - LinuxBook,None,Stephen A. Rago,有关于 Linux 的书籍,UNIX环境高级编程,人民邮电出版社,9.5
        Book - fnc: <module>() - line: 244 - DEBUG - 插入后，使用对象查找对象
        Book - fnc: find() - line: 119 - INFO - 找到 id = 7 的对象: LinuxBook,None,Stephen A. Rago,有关于 Linux 的书籍,UNIX环境高级编程,人民邮电出版社,9.5
        Book - fnc: <module>() - line: 245 - DEBUG - LinuxBook,None,Stephen A. Rago,有关于 Linux 的书籍,UNIX环境高级编程,人民邮电出版社,9.5
        Process finished with exit code 0
        ```
