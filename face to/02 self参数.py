# 类中方法的调用顺序

class Cat:
    def eat(self):
        print("eat---self：",self)
    def drink(self,water):
        print("drink---self:",self)
        print("喝：%s" % water)

TOM=Cat()
print(TOM)
TOM.eat()
TOM.drink("milk")
