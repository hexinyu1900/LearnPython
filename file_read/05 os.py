import os

# os.rename("hi.txt" ,"new.txt")
# os.remove("renew.txt")

# # 目录列表
# # 查看指定目录下所有文件名和目录名，以列表的形式展现，默认获取的是当前目录
# print(os.listdir("E:\\file_read"))
# print(os.listdir("."))
# print(os.listdir())

# # 创建目录
# os.mkdir("bug")

# # 删除目录
# # rmdir()只能删除空目录
# # 拓展：stutil模块中，用rmtree()方法删除非空目录
# os.rmdir("bug")

# 获取当前目录
print(os.getcwd())

# # 修改工作目录（修改的是python解释器的工作目录）
# os.chdir("000")
# print(os.getcwd())

# 判断是否是文件夹
# 如果是目录，返回True，否则返回False
print(os.path.isdir("000"))

# 判断目录或者文件是否存在，如果存在，返回True，否则返回False
print(os.path.exists("000"))