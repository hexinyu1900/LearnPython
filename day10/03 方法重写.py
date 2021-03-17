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
    # 功能覆盖
    # def catch(self):
    #     """抓鱼方法"""
    #     print("波斯猫抓鱼吃")

    # 功能扩展
    def catch(self):
        # ①super().重写的方法名()
        # super().catch()
        # ②父类名.方法名(self)  #不推荐使用，父类名修改后，在调用的地方也需要修改父类名
        Cat.catch(self)
        print("波斯猫抓鱼吃")

boss = BossCat()
# 子类重写了父类的方法后，调用方法时，调用的是自己重写后的方法
boss.catch()

