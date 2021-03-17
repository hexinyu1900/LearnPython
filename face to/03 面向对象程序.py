# 类中方法的调用顺序

class Cat:
    def eat(self):
        print("eat")
    def drink(self):
        print("drink")

TOM=Cat()
print(TOM)
TOM.eat()
TOM.drink()
Cat().drink()