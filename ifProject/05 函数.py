# # 定义函数
# def say_hello():
#     '''
#     一个函数的文档注释
#     :return:
#     '''
#     print("你好")
#     print("hello")
#     print("hi")
# # 调用函数
# say_hello()
# # 查看注释
# help(say_hello)

# def sum_2_num():
#     '''
#     当前函数实现两个数字求和功能
#     :return:
#     '''
#     num1 = int(input("请输入第一个加数："))
#     num2 = int(input("请输入第二个加数："))
#     sum = num1+num2
#     print("%d + %d = %d" % (num1, num2, sum))
#
# sum_2_num()


def sum_2_num(num1, num2):
    '''
    当前函数实现两个数字求和功能
    :return:
    '''
    sum = num1 + num2
    print("%d + %d = %d" % (num1, num2, sum))
    return sum

sumaa = sum_2_num(20, 50)
print("----result:", sumaa)
