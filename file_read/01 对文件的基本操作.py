# 1.打开文件
# 文件不存在，报错
# 注意：Windows默认编码格式gbk，打开文件需要指定编码格式，encoding='UTF-8'
#      linux和unix系统默认编码格式就是utf-8
file=open("new.txt",'r', encoding='UTF-8')

# 2.操作文件
# read()方法一次性读取文件全部内容，下次再读取时，将读不到任何内容
text=file.read()
print("------>>>%s<<<--------" % text)
print(type(text))

# 3.关闭文件
# 不关闭文件会造成系统资源浪费
file.close()