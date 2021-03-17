# 特点：打印对象时，自动调用print(对象名)
# 作用：打印对象的描述信息
# 注意：__str__方法必须有返回值，只能返回字符串

class cat:
    """猫类"""
    def __init__(self, name):
        """初始化方法"""
        self.name = name

    def eat(self):
        """吃方法"""
        print("%s 爱吃小鱼干" % self.name)

    def __str__(self):
        """对象描述信息方法"""
        print("使用print()方法，打印对象时自动调用")
        return "名字是：%s" % self.name
blue = cat("蓝猫")
print(blue)