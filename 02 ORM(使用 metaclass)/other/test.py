import re

a = '9,《入理解计算机系统（原书第2版）》,9.7,1196,（美）Randal E.Bryant / David,机械工业出版社 / 2011-1-1 / 99.00元\n10,《入理解计算机系统（原书第2版）》,9.7,1196,（美）Randal E.Bryant / David,机械工业出版社 / 2011-1-1 / 99.00元\n'
text = re.sub("%d,.*" % 10, "test", a)
print(text)