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

    @staticmethod
    def func_static():
        """静态方法"""
        print("1.静态方法中不需要self参数，也不需要cls参数")
        print("2.静态方法中不需要实例属性，也不需要类属性")
        print("3.静态方法中不需要实例方法，也不需要类方法")
        print("4.静态方法还不能破坏类的封装性")

# 调用静态方法
# 类名.静态方法名()
Person.func_static()
print("----------")
# 实例对象.静态方法名()
rdj = Person("RDJ")
rdj.func_static()
