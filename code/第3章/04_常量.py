"""
常量是指在程序运行过程中其值不应该改变的变量。常量通常使用全大写字母来命名，以区分于普通变量。
虽然Python没有内置的常量类型，但通过命名约定和代码规范，我们可以将某些变量视为常量。
"""

ADULT_AGE = 18
MONTHS_IN_YEAR = 12
MAX_USERS = 1200
PASSING_SCORE = 60
MAX_USERS = 1300  # 修改常量的值，虽然语法上没有错误，但不符合常量的定义和使用规范

print(ADULT_AGE, MONTHS_IN_YEAR, MAX_USERS, PASSING_SCORE)
