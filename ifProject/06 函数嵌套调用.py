def demo02():
    print("-------demo02函数调用开始------")
    print("-------demo02函数的中间执行过程")
    print("-------demo02函数调用结束------")

def demo01():
    print("-------demo01函数调用开始------")
    demo02()
    print("-------demo01函数的中间执行过程")
    print("-------demo01函数调用结束------")

demo01()

#使用模块中的函数
import  modei_test
modei_test.mutiple_table()