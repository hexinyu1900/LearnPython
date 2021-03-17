# 1.打开文件
file=open("new.txt",'r', encoding='UTF-8')

# 2.操作文件
while True:
    line_text=file.readline()
    print(line_text)
    if len(line_text)==0:
        break


# 3.关闭文件
file.close()