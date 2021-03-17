# my_dict = {'name': '南宫问天', 'age': 17, 'gender': '男', 'high': 180}
# print(my_dict)
# # 字典的访问
# # 字典不能通过索引访问，字典是无序的数据容器
# # 注意：字典是通过键来访问的
# # 字典名[键]
# print(my_dict['name'])

info_dict = {
    'name': '兰陵王',
    'age': 30,
    'height': 180,
    'gender': '男'
}
print("字典操作前：", info_dict)
#
# # 字典名[key] key存在，取对应的value值，key不存在，报错 (报错，后面的代码不执行)
# print(info_dict['name'])
# # 字典名.get(key)  key存在，取对应的value值，key不存在，不会报错，返回None（后面的代码执行）
# print(info_dict.get('name'))
# print(info_dict.get('sex'))
# print(info_dict.get('sex', '你是谁'))
# print(info_dict.get('age'))


# # 字典名[key]=新值  key存在，修改对应value值，key不存在，新增键值对
# info_dict['age']=22
# info_dict['addr']='苍牙池'
# print(info_dict)

# #字典名.setdefault(key,value)   key存在，不修改对应value值，使用默认值；key不存在，新增键值对
# info_dict.setdefault('addr','山')
# print(info_dict)
#
# # 字典1.update(字典2)  把字典2合并到字典1，key存在，更新对应的value值，key不存在，新增键值对
# info_dict.update({'addr':'海'})
# print(info_dict)

# # del 字典名[key]   key存在，正常删除键值对，key不存在，报错
# del info_dict['age']
# print(info_dict)
# # 字典名.pop(key)   key存在，正常删除键值对，key不存在，报错
# info_dict.pop('gender')
# print(info_dict)

# # 字典名.clear()    #清空字典
# info_dict.clear()
# print(info_dict)

# 统计字典中键值对的个数
print(len(info_dict))

