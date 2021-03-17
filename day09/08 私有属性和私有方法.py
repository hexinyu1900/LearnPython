class Women:
    """定义一个类"""
    def __init__(self, name):
        """初始化方法"""
        self.name = name
        # 前置双下划线的属性是私有属性
        self.__age = 20

    def eat(self):
        """吃方法"""
        # 在类的内部可以通过self访问私有属性
        print("%s 今年%d岁，是一个吃货" % (self.name, self.__age))
        self.__secret()

    def __secret(self):
        """私有方法"""
        # 前置双下划线的方法是私有方法
        print("个人秘密，不方便透露……")

marry = Women("玛丽")
print(marry.name)
# 在类的外部无法直接访问私有属性
# print(marry.__age)

marry.eat()
# 在类的外部无法直接访问私有方法
# marry.__secret()