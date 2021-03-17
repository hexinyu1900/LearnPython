class Women:
    """定义一个类"""
    def __init__(self, name):
        """初始化方法"""
        self.name = name
        # 前置双下划线的属性是私有属性
        self.__age = 20

    # 对外提供访问私有属性的接口（方法） get/set
    def get_age(self):
        """获取私有属性值"""
        return self.__age

    def set_age(self, new_age):
        """设置私有属性值"""
        if new_age <= 0 or new_age >= 150:
            print("您输入的年龄有误")
            return
        self.__age = new_age

    def eat(self):
        """吃方法"""
        # 在类的内部可以通过self访问私有属性
        print("%s 今年%d岁，是一个吃货" % (self.name, self.__age))
        # self.__secret()

    def __secret(self):
        """私有方法"""
        # 前置双下划线的方法是私有方法
        print("个人秘密，不方便透露……")

marry = Women("玛丽")
# print(marry.name)
# 在类的外部无法直接访问私有属性
# print(marry.__age)

# marry.eat()
# 在类的外部无法直接访问私有方法
# marry.__secret()

print(dir(marry))

# python中并没有真正意义上的私有，是通过名字重整的方式，把私有属性和私有方法改了名字
# 私有属性    __私有属性名 ==》 _类名__私有属性名
# 私有方法    __私有方法名 ==》 _类名__私有方法名
# print(marry._Women__age)             # 在类的外部无法直接访问私有属性，可以通过名字重整的方式，简介访问
# print(marry._Women__secret())        # 在类的外部无法直接访问私有方法，可以通过名字重整的方式，简介访问

ret = marry.get_age()
print(ret)

marry.set_age(25)
ret = marry.get_age()
print(ret)