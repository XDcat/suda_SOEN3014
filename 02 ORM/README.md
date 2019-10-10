## 如何运行示例代码
```angular2
cd 02 ORM
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
       cd 02 ORM
       python ./Book.py
        ```
     3. 结果展示
         ```
          D:\CS\anaconda\envs\py3\python.exe "D:/Box/Pycharm_Project/工业实践课程/02 ORM/Book_new.py"
        Book_new - fnc: find() - line: 108 - INFO - 并没有找到 id = d6d5d4fa-eb61-11e9-a9f4-5800e3b9e508 的记录
        Book_new - fnc: save() - line: 58 - INFO - 无法更新: 文件中没有 id = d6d5d4fa-eb61-11e9-a9f4-5800e3b9e508 的记录
        Book_new - fnc: find() - line: 108 - INFO - 并没有找到 id = d6d5d4fa-eb61-11e9-a9f4-5800e3b9e508 的记录
        Book_new - fnc: add() - line: 41 - INFO - 插入对象:LinuxBook,d6d5d4fa-eb61-11e9-a9f4-5800e3b9e508,Stephen A. Rago,有关于 Linux 的书籍,./data/,./data/LinuxBook.txt,UNIX环境高级编程,人民邮电出版社,9.5
        Book_new - fnc: find() - line: 106 - INFO - 找到 id = d6d8e026-eb61-11e9-a224-5800e3b9e508 的对象: LinuxBook,d6d8e026-eb61-11e9-a224-5800e3b9e508,9.5,./data/,./data/LinuxBook.txt,,有关于 Linux 的书籍,./data/,./data/LinuxBook.txt,,,,有关于 Linux 的书籍
        Book_new - fnc: save() - line: 56 - INFO - 更新 id = d6d5d4fa-eb61-11e9-a9f4-5800e3b9e508 的记录
        Book_new - fnc: find() - line: 106 - INFO - 找到 id = d6d97bfa-eb61-11e9-85b8-5800e3b9e508 的对象: LinuxBook,d6d97bfa-eb61-11e9-85b8-5800e3b9e508,9.5,./data/,./data/LinuxBook.txt,,有关于 Linux 的书籍,./data/,./data/LinuxBook.txt,,,,有关于 Linux 的书籍
        Book_new - fnc: destroy() - line: 72 - INFO - 删除对象:LinuxBook,d6d5d4fa-eb61-11e9-a9f4-5800e3b9e508,Stephen A. Rago,有关于 Linux 的书籍,./data/,./data/LinuxBook.txt,UNIX环境高级编程,人民邮电出版社,9.5
        Book_new - fnc: find() - line: 108 - INFO - 并没有找到 id = d6d5d4fa-eb61-11e9-a9f4-5800e3b9e508 的记录
        Book_new - fnc: find() - line: 108 - INFO - 并没有找到 id = d6d5d4fa-eb61-11e9-a9f4-5800e3b9e508 的记录
        None
        None
        Book_new - fnc: find() - line: 108 - INFO - 并没有找到 id = d6d5d4fa-eb61-11e9-a9f4-5800e3b9e508 的记录
        Book_new - fnc: add() - line: 41 - INFO - 插入对象:LinuxBook,d6d5d4fa-eb61-11e9-a9f4-5800e3b9e508,Stephen A. Rago,有关于 Linux 的书籍,./data/,./data/LinuxBook.txt,UNIX环境高级编程,人民邮电出版社,9.5
        Book_new - fnc: find() - line: 106 - INFO - 找到 id = d6db4f7a-eb61-11e9-88e2-5800e3b9e508 的对象: LinuxBook,d6db4f7a-eb61-11e9-88e2-5800e3b9e508,9.5,./data/,./data/LinuxBook.txt,,有关于 Linux 的书籍,./data/,./data/LinuxBook.txt,,,,有关于 Linux 的书籍
        Book_new - fnc: find() - line: 106 - INFO - 找到 id = d6dbc45e-eb61-11e9-845e-5800e3b9e508 的对象: LinuxBook,d6dbc45e-eb61-11e9-845e-5800e3b9e508,9.5,./data/,./data/LinuxBook.txt,,有关于 Linux 的书籍,./data/,./data/LinuxBook.txt,,,,有关于 Linux 的书籍
        LinuxBook,d6db4f7a-eb61-11e9-88e2-5800e3b9e508,9.5,./data/,./data/LinuxBook.txt,,有关于 Linux 的书籍,./data/,./data/LinuxBook.txt,,,,有关于 Linux 的书籍
        LinuxBook,d7dbc45e-eb61-11e9-845e-5800e3b9e508,9.5,./data/,./data/LinuxBook.txt,,有关于 Linux 的书籍,./data/,./data/LinuxBook.txt,,,,有关于 Linux 的书籍

        Process finished with exit code 0
        ```
