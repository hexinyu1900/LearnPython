# 定义类模板
class cat:
    def __init__(self, new_name):
        self.name = new_name
    def eat(self):
        print("---%s  eat fish---" % self.name)

# 使用类模板创建对象
tom = cat("汤姆猫")
tom.eat()
jerry = cat("鼠猫")
jerry.eat()