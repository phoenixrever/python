# 所谓整型，就是没有小数点的数字，可以是正数，也可以是负数，也可以是0。
import sys

age = 18
temp = -15
score = 0

# 当数很大时，我们可以使用下划线将数字进行分组，来让数字变得更易读。
salary = 300_000
house_price = 3_200_000
graduates = 12_000_000
print(salary, house_price, graduates)

# Python中整数的上限值，取决于执行代码的计算机的内存和处理能力。
a = 9**9999
# sys.set_int_max_str_digits() 是 Python 3.11 才加入的安全 API。 注意右下角的 Python 版本，必须是 3.11 或更高版本才能使用这个函数。
sys.set_int_max_str_digits(
    0
)  # 设置整数转字符串的最大字符串长度为0，表示没有限制 默认是4300 ，但是我默认没设置也没限制
print(a)
