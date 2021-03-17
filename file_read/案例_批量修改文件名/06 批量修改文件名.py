import os
import shutil
# # 1、批量创建文件
# def create_files():
#     print(os.getcwd())
#     # （1）先创建目录files
#     if os.path.exists("./files"):
#         shutil.rmtree("./files")
#     os.mkdir("./files")
#     # （2）将工作目录切换到files目录下
#     os.chdir("./files")
#     print(os.getcwd())
#     # （3）在files目录下批量创建文件
#     for i in range(1, 21):
#         file=open("new"+str(i)+".txt", "w", encoding="utf-8")
#         file.write("你好啊")
#         file.close()
# create_files()

# 2、批量修改文件名
def change_files_name():
    # 查看当前的目录是否为files，若不是，切换到files目录下
    print(os.getcwd())
    path="E:\\file_read\\案例_批量修改文件名\\files"
    if os.getcwd() != path:
        os.chdir(path)
        print(os.getcwd())
    # 如果是files目录下，获取目录所有的内容，以列表方式保存
    files_name=os.listdir()
    print(files_name)
    # 使用for循环遍历列表
    for name in files_name:
        print(name)
        os.rename(name, "001"+name)


change_files_name()