class Father:
    def __init__(self):
        # 普通的属性，公有属性
        self.name = "RDJ"
        # 前置双下划线的属性是私有属性
        self.__password = 123456

    # 在类的内部对外提供访问私有属性的接口 get/set
    def get_pwd(self):
        """获取私有属性"""
        return self.__password

    def set_pwd(self,new_pwd):
        """设置私有属性"""
        self.__password = new_pwd

    def func_secret(self):
        """调用私有方法"""
        self.__secret()

    def eat(self):
        print("%s 爱吃巧克力" % self.name)

    def __secret(self):
        """私有方法"""
        # 前置双下划线的方法是私有方法
        print("%s 的个人秘密，设备密码是：%d" % (self.name, self.__password))

class Son(Father):
    def run(self):
        print("spider man")


tom = Son()
tom.run()
print(tom.name)

# 在类外，子类对象无法直接访问父类的私有属性