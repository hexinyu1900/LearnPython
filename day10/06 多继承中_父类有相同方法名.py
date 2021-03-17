class Horse:
    """马类"""
    def run(self):
        """跑方法"""
        print("马跑得快")
    def walk(self):
        """走方法"""
        print("马走不远")

class Donkey:
    """驴类"""
    def walk(self):
        """走方法"""
        print("驴走得远")
    def run(self):
        """跑方法"""
        print("驴跑不快")

class Mule(Horse, Donkey):
    """骡子类"""
    pass

mule = Mule()
mule.run()
mule.walk()

# __mro__方法解析顺序
print(Mule.__mro__)
# 多继承，父类有相同的方法名，参考__mro__方法解析顺序来调用