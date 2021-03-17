a = 6
b = 100
print("交换前 a=%s,b=%s" % (a, b))

# 1、使用临时变量
temp = a
a = b
b = temp
print("a=%s" % a)
print("b=%s" % b)
# 2、计算法
a = a + b
b = a - b
a = a - b
print("a=%s" % a)
print("b=%s" % b)
# 3、python中特有，使用元组
b, a = ret = a, b
print(ret)
print(type(ret))
print("a=%s" % a)
print("b=%s" % b)
