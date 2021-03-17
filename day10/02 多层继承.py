class Animal:
    """动物类（父类）"""
    def __init__(self):
        """初始化方法"""
        self.name = "动物"
        self.age = 2

    def eat(self):
        """吃方法"""
        print("%s 都爱吃" % self.name)

class Cat(Animal):    #单继承  子类（父类）
    """猫类"""
    def catch(self):
        """抓老鼠方法"""
        print("猫捉老鼠")

class BossCat(Cat):
    """波斯猫类"""
    def sing(self):
        print("猫可以喵喵喵")

boss = BossCat()
print(boss.name)
boss.sing()