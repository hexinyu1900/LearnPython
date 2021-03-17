# __del__方法:
# 当前程序退出时，对象从内存空间销毁前，自动调用
# 作用：清除资源的操作

class cat:
    """猫类"""
    def __init__(self, name):
        """初始化方法"""
        self.name = name

    def eat(self):
        """吃方法"""
        print("%s 爱吃小鱼干" % self.name)

    def __del__(self):
        """删除的魔法方法"""
        print("当前程序退出时，对象从内存空间销毁前，自动调用")
        print("清除资源的操作")

carry = cat("加菲猫")

# 注意：__del__魔法方法在程序退出之前自动调用
#      __del__魔法方法可以手动使用

del carry
# print(carry.name)    #对象内存空间已经被销毁，不能访问属性