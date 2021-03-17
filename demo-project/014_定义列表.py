# mylist = [100, 2.3, 3, 'hello', '中国人']
# print(mylist)
# print(type(mylist))
#
# print(mylist[1])

# # 列表的快速格式化 ctrl+alt+l  alt+shift+enter
# info_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print("原来的列表是：", info_list)

# 增
# 列表.insert(索引,数据)  在指定位置插入数据
# info_list.insert(0, 100)
# print(info_list)
# # 列表.insert()  插入小列表
# info_list.insert(8, [200, 900])
# print(info_list)
# # 列表.append(数据)   在末尾追加数据
# info_list.append(200)
# print(info_list)
# # 列表1.extend(列表2)    将列表2的数据追加到列表1
# info_list.extend([500,600])
# print(info_list)

# # del 列表[索引]     删除指定索引的数据
# del info_list[0]
# print(info_list)

# # 把列表从内存清除
# del info_list

# # 列表.remove(数据) 删除第一个出现的指定数据
# info_list.remove(4)
# print(info_list)

# # 列表.pop()   删除末尾数据（返回删除的数据）
# num=info_list.pop()
# print(num)
# print(info_list)
# # 列表.pop(索引)  删除指定索引数据（返回删除的数据）
# num=info_list.pop(2)
# print(num)
# print(info_list)


# # 列表.clear() 请空列表
# info_list.clear()
# print(info_list)

# # 列表[索引]=数据  修改指定索引的数据
# # 列表中的数据可以修改
# info_list[0]=111
# print(info_list)

# # 列表名[索引]   通过索引获取数据
# print(info_list[2])

# # 通过数据获取索引
# # 列表名.index(数据)   获取数据在列表中第一次出现的索引值
# print(info_list.index(5))


my_list = [1, 2, 3, 5, 4, 8, 54, 4, -54, 54, 54, 1, 3, 0]
print("原来的列表是：", my_list)
# # 统计
# # len(列表)  列表长度（列表中元素个数）
# print(len(my_list))
# # 列表.count(数据)  数据在列表中出现的次数
# print(my_list.count(54))
# print(my_list.count(500))       #没有这个数据，返回0

# # 排序
# # 列表.sort()  升序排序（从小到大排序）
# my_list.sort()
# print(my_list)

# # 列表.sort(reverse=True)   降序排序（从大到小进行排序）
# my_list.sort(reverse=True)
# print(my_list)

# # 列表.reverse()  逆序、反转
# # 反转：前面的数据放到后面，后面的数据放到前面
# my_list.reverse()
# print(my_list)

# # 列表拷贝
# # 列表名.copy()
# # id()函数可以查看变量保存数据的内存地址
# new_list = my_list.copy()
# print(my_list, id(my_list))
# print(new_list, id(new_list))
