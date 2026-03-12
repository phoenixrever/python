# 使用 \' 输出 '
# print('在Python中，可以使用\'包裹一个字符串')

# 使用 \" 输出 "
# print("在Python中，可以使用\"包裹一个字符串")

# 使用 \n 进行换行
# print('注册会员需要以下信息：\n姓名\n年龄\n手机号')

# 使用 \\ 输出 \
# print('D:\\nice')

# 使用 \b 删除前一个字符 可以用来实现退格打印机动画效果
# print('helloo\b')

# 使用 \r 使光标回到本行开头，覆盖输出 可以用来实现进度条动画效果 10% 20% 30% ... 100% 这样命令行种数字不断变化就是这样实现的
# print('67%\r68%')

# 使用 \t 表示水平制表符（让光标跳转到下一个制表位） 制表位的距离是固定的，
# pycharm是4个字符的位置，cmd终端是8位置，所以 \t 的效果取决于前面已经输出了多少字符
# 一个制表位到底是几位，是不确定的，但我们可以通过在字符串后面加.expandtabs()来指定位数。
print('1234123412341234')
print('ab\tcd'.expandtabs(4))
print('abc\td'.expandtabs(4))
print('abcd\ta'.expandtabs(4))
print('我是\t中文'.expandtabs(4))

print('12341234123412341234')
print('姓名\t性别\t年龄')
print('张三\t男\t\t18')
print('李四\t女\t\t25')
print('王五\t男\t\t32')
