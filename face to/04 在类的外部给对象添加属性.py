# 给对象添加属性：
# 1.在类的外部给对象添加属性
#   对象名.属性名=属性值
# 2.在类的内部给对象添加属性

# 定义类模板
class Cat:
    def eat(self):
        # 在类的内部访问属性  通过self.属性名
        print("----%s eat-----" % self.name)
        # 在类的内部访问方法  通过self.方法名(参数)
        self.drink("雪碧")

    def drink(self,water):
        print("drink:%s" % water )

# 通过类模板创建对象
tom = Cat()

# 在类外给对象添加属性
# 对象名.属性名=属性值
tom.name = "汤姆猫"

# 在类的外部访问属性
# 对象名.属性名
print(tom.name)
tom.eat()

