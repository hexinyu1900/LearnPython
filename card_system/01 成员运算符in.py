# 作用：判断一个数据是否为数据容器中的成员
# 如果是返回Ture，否则返回False

info = [10,20,30]

print(10 in info)
print(5 in info)

if 80 in info:
    print("该数据是列表成员")
else:
    print("该数据不是列表成员")
