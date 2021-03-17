str="hello,python,python"

# # 判断
# # string.startswith(str) 检查字符串是否以str开头，是则返回True
# print(str.startswith('h'))
# print(str.startswith('python'))
# # string.endswith(str) 检查字符串是否以str结束，是则返回True
# print(str.endswith('n'))
# print(str.endswith('java'))
# # 应用：查找以.py结尾的文件或以.html结尾的文件


# print(str.find('e'))   # 已经找到，返回索引值
# print(str.find('hello'))     # 返回最左边第一个字符串的索引
# print(str.find('python', 8))    # 指定开始范围，从8索引向后找
# print(str.find('python', 8, len(str)))     # 指定范围
# print(str.find('java'))    #没有找到，返回-1
# # print(str.index('java', 0, len(str)))           # 报错

# 字符串的替换
print(str.replace('python','go'))    #num值没有指定，默认全部替换
print(str.replace('python', 'go', 1))    #num值指定为1，替换1次

