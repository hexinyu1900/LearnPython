# __del__方法:
# 当前程序退出时，对象从内存空间销毁前，自动调用
# 作用：清除资源的操作，文件的资源，网络套接字资源，数据库连接资源

class cat:
    """猫类"""
    def __init__(self, name):
        """初始化方法"""
        self.name = name

    def eat(self):
        """吃方法"""
        print("%s 爱吃小鱼干" % self.name)
        # 局部变量作用范围只能是当前方法，如果想让下面的方法访问到当前的局部变量，需要把局部变量保存为属性
        # 1.打开文件
        self.file = open("cat.txt", "w", encoding="utf-8")
        # 2. 操作文件
        self.file.write("%s 爱吃小鱼干" % self.name)



    def __del__(self):
        """删除的魔法方法"""
        print("当前程序退出时，对象从内存空间销毁前，自动调用")
        print("清除资源的操作")
        print("--1--文件关闭前-----")
        # 3.关闭文件
        self.file.close()
        print("--2--文件关闭后-----")

carry = cat("加菲猫")
carry.eat()

# 注意：__del__魔法方法在程序退出之前自动调用
#      __del__魔法方法可以手动使用

