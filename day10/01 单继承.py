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

# 使用父类模板创建对象
animal = Animal()
# 父类的对象可以访问自己的属性
print(animal.name)
# 父类的对象可以调用自己的方法
animal.eat()
# 父类对象无法调用子类的方法，也不能访问子类的属性
# animal.catch()

print("-"*50)
# 使用子类模板创建对象
tom = Cat()
# 子类对象可以访问父类的属性
print(tom.name)
print(tom.age)
# 子类对象可以调用父类的方法
tom.eat()

# 继承不是复制
# 访问子类属性时，先到子类中查找
# 子类中没有该属性，则去父类中查找