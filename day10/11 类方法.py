class Person:
    count = 0
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("%s 爱吃美食" % self.name)

    @classmethod
    def get_count(cls):
        print("1.类方法的作用：处理类属性或调用其他类方法")
        print("2.cls参数保存的是当前类对象的引用，cls：", cls)
        cls.count += 100
        return cls.count


print(Person)
# 调用类方法
# 类对象名.类方法名()
# Person.get_count()
ret = Person.get_count()
print(ret)