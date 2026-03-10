"""
#coding=Shift_JIS  解码用,读取的时候用Shift_JIS 来读 字符串会乱码

📋备注：在 Python3 中，可以不写文件编码声明，因为 Python3 默认就使用 UTF-8 编码。

📢注意：Python 中并没有真正的多行注释语法，所谓多行注释的本质其实还是字符串
"""

# name是张三的名字
name = '张三'
# age是张三的年龄
age = 18
# weight是张三的体重（单位：kg）
# 张三的体重还可以
weight = 65.2

print(name, age, weight)  # 下面是一句打印

"""
下面是一些常量
ADULT_AGE是法定成人年龄
MONTHS_IN_YEAR是一年中的几个月
MAX_USERS是最大同时在线人数
"""
ADULT_AGE = 18
MONTHS_IN_YEAR = 12
MAX_USERS = 1200
print(ADULT_AGE, MONTHS_IN_YEAR, MAX_USERS)
