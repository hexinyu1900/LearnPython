class Person:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("%s 爱吃美食" % self.name)


# 创建的对象在内存空间中实际存在，叫做实例对象
RDJ = Person("RDJ")
print(RDJ)
print(RDJ.name)  # 实例对象中的属性是实例属性
print("id(RDJ.name):", id(RDJ.name))
RDJ.eat()  # 属于实例对象的方法，并且具有self参数，是实例方法
print("id(RDJ.eat):", id(RDJ.eat))
