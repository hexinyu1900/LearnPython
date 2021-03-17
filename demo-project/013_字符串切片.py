# 作用：从大字符串中快速切出小字符串


# 使用切片
# 切出字符串hello
info_str="hello python"
print(info_str[0:5:1])
print(info_str[0:5:])     #步长正1时可以省略
print(info_str[0:5])      #步长正1时可以省略，步长前面的冒号可以省略
print(info_str[:5])       #开始位置索引是字符串的边界，开始位置索引可以省略
# 切出字符串python
print(info_str[6:12:1])
print(info_str[6:])       #结束位置索引是字符串的边界，结束位置索引可以省略
# 倒序切片 步长是负数
print(info_str[-1:-7:-1])
print(info_str[11:5:-1])
print(info_str[:5:-1])

print(info_str[-1:-13:-1])

print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))

# 通过字典设置参数
site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{name}, 地址 {url}".format(**site))

# 通过列表索引设置参数
my_list = ['菜鸟教程', 'www.runoob.com']
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的

