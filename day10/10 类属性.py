# 类模板就是一个对象，简称类对象
class Person:
    # 类属性，定义在方法外边，类的内部
    # 作用：主要用来记录类对象的相关特征
    count = 0  # 类属性只是被初始化一次
    print("类模板初始化一次")

    def __init__(self, name):
        # 实例属性
        self.name = name
        print("------初始化方法__init__------")
        # 使用类属性统计当前类模板创建了几个实例对象
        # 访问类属性，使用类名.
        Person.count += 1

    def eat(self):
        print("%s 爱吃美食" % self.name)


# 使用类模板 创建实例对象
rdj = Person("RDJ")
tom = Person("SPIDER")
thor = Person("GOD")

# 类外访问类属性
# ①类名.类属性名
print("当前创建的实例对象个数：", Person.count)
# ②实例对象.类属性名
print("tom.count:", tom.count)
# 修改类属性
# 类名.类属性 = 值
Person.count = 10
print("当前创建的实例对象个数：", Person.count)
# 
