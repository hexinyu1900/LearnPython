# 目标：实现多态

class Dog:
    def __init__(self, name):
        self.name = name
    def game(self):
        print("%s 简单玩" % self.name)

class Skydog(Dog):
    def __init__(self, name):
        self.name = name
    def game(self):
        print("%s 天上玩" % self.name)

class Person:
    def __init__(self, name):
        self.name = name

    def play_with_dog(self, dog):
        print("%s 和 %s 一起玩耍" % (self.name, dog.name))
        # 不同的对象调用相同的方法，产生不同的结果状态，叫做多态
        dog.game()

waicai = Dog("旺财")
xiaotian = Skydog("啸天")
jay = Person("jay")
jay.play_with_dog(xiaotian)
