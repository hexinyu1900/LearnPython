# 定义类
class Person:
    def run(self):
        print("跑")
    def eat(self, food):
        print("吃：%s" % food)
# 使用类模板创建对象
# 对象变量=类名()
marry = Person()
# 通过对象调用方法
# 对象变量名.方法名()
# 注意：调用方法时，self参数不需要我们传递，由python解释器自动传递
marry.eat("饺子")