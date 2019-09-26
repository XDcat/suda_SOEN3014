## 如何运行实例
```angular2
cd 02 ORM
python ./Book.py
```

## 说明
1. data 文件夹，存放着数据存储文件以及存有一些样本数据 excel 文件
2. Book.py 文件
    1. Book 类，对数据进行操作，具体如下
        * 增：初始化对象后，调用 `save()`
        * 删：使用 `delete(id)`
        * 改：修改对象后，使用 `update`
        * 查：使用 `query(id)`
    2. main 函数，使用 Book 类的一些例子
        ```angular2
       cd 02 ORM
       python ./Book.py
        ```