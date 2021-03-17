# print(range(0, 10, 1))
# for i in range(2,10,2):
#     print(i)
# print('*' * 50)
# for n in range(10,0,-1):
#     print(n)

# 使用列表推导式 生成一个列表
print([x for x in range(0, 5, 1)])
# 使用列表推导式，生成一个列表，range函数步长为2
print([n for n in range(1, 11, 2)])
# 使用列表推导式，生成一个列表，变量的值都需要加100
print([z for z in range(10)])
print([z + 100 for z in range(10)])
# 使用列表推导式，生成一个列表，变量的值是变量与变量的乘积
print([y * y for y in range(10)])


# 列表推导式中可以添加条件判断
# 使用列表推导式，生成0~20范围内的偶数列表，不允许使用步长2
print([a for a in range(21)])
print([b for b in range(21) if b % 2 == 0])

# 创建包含100个随机数的列表
import random
new_list=[random.randint(0, 100) for x in range(100)]
print(new_list)
# 将上面列表中的元素加100
print([n + 100 for n in new_list])
# 序列中所有偶数组合成列表
print([p for p in new_list if p % 2 == 0])

13 19
14 20
15 21
16 22
17 23
18 24
19 25
20 26