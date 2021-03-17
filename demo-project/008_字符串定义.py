# 1.成对的双引号或成对的单引号
str1="we are groot!"
print(type(str1))
str2='we are family!'
print(type(str2))

# 拓展
# 成对的双引号中可以嵌套成对的单引号
# 成对的单引号中可以嵌套成对的双引号
info="你是一个'好人'"
print(info)

# 2.成对的三个双引号或成对的三个单引号
str3="""我是字符串"""
str3_1="""我是字符串，你是"好人"，你真的是'好人'吗"""
print(str3)
print(str3_1)
str4='''我也是字符串'''

# 3.定义字符串的特殊形式（原生字符串）（正则表达式）
str5="I\'m person"
str5=r"I\'m person"
print(str5)