# # 定义元组
# my_tuple = (100, 15.6, True, "python", 20, "中文")
# print(my_tuple)
# print(type(my_tuple))

# # 定义只有一个数据的元组,需要加逗号
# my_tuple = (21,)
# print(my_tuple)
# print(type(my_tuple))

my_tuple = (100, 15.6, True, "python", 20, "中文",[20,45])

# # 访问元组中数据
# # 通过索引访问数据：元组名[索引值/下标]
# print(my_tuple[0])
# # 修改元组中的数据，是受到限制的
# # 元组中的数据不允许修改，但是如果元组中有列表和字典，则列表和字典中的数据可以修改
# small_list=my_tuple[6]
# print(small_list)
# small_list[0]=10000
# print(my_tuple)

# # 通过索引获取数据
# # 格式：元组名[索引值]
# print(my_tuple[3])

# # 通过数据获取索引
# # 格式：元组名.index(数据)    数据不存在时报错
# print(my_tuple.index("中文"))

# # 统计元组中某个数据出现的次数
# # 元组名.count(数据)
# print(my_tuple.count(100))

# 统计元组的长度
# len(元组名)
print(len(my_tuple))