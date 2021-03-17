class Person:
    """人类"""
    def __init__(self, name, weight):
        """初始化方法"""
        self.name = name
        self.weight = weight

    def __str__(self):
        """打印对象的描述信息"""
        return "姓名是：%s 体重是：%.2f" % (self.name, self.weight)

    def run(self):
        """跑方法"""
        print("%s每次跑步会减肥0.5公斤" % self.name)
        self.weight -= 0.5

    def eat(self):
        """吃方法"""
        print("%s每次吃东西体重增加1公斤" % self.name)
        self.weight += 1

ming = Person("小明", 75.0)
print(ming)

ming.run()
print(ming)

ming.eat()
print(ming)
