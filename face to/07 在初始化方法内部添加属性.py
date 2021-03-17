# 定义类模板
class cat:
    def __init__(self):
        """初始化方法"""
        print("1.__init__初始化方法主要用来初始化数据")
        # 在类的内部添加属性 self.属性名 = 属性初始值
        self.name = "汤姆猫"
        print("2.初始化方法在使用类模板创建对象时自动调用")
    def eat(self):
        print("---%s  eat fish---" % self.name)
# 使用类模板创建对象
tom = cat()
# 在类的外部访问属性 对象名.属性名
print(tom.name)
# 在类的外部调用 对象名.方法名()
tom.eat()