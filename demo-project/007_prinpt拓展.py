name="昊辰"
age=2222
gender="男"
height=185

# 一行输出
print(name,age,gender,height)

# print()函数默认自带换行
print("----------1----------")
print('----------2----------')

# 占位符：%d(数字) %s(字符串) %f(浮点数，小数) %%(两个%表示一个%)
# 格式： print("字符串信息 占位符" % 变量或数据)
print("姓名：%s" % name)
print("年龄：%d" % age)
print("身高：%f" % height)
print("身高：%.1f" % height)

# 格式化输出
print("姓名：%s,年龄：%d,身高：%.1f" % (name,age,height) )