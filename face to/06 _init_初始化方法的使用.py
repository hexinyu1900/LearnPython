# 定义类模板
class cat:
    def __init__(self):
        """初始化方法"""
        # __init__初始化方法主要用来初始化数据
        # 初始化属性数据
        # 初始化方法在使用类模板创建对象时自动调用
        print("1.__init__初始化方法主要用来初始化数据")
        print("2.初始化方法在使用类模板创建对象时自动调用")
    def eat(self):
        print("---eat fish---")

tom = cat()