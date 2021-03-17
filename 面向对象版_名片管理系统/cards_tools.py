# 当前文件负责各个功能函数的实现和定义
# 实现的功能：显示菜单 新建名片 显示全部名片 查询名片 修改名片 删除名片
import os


class CatdsTool:
    """名片功能类"""

    def __init__(self):
        """初始化方法"""
        # 定义全局变量 名片列表
        self.card_list = [
            # {'name': '张起灵', 'tel': '110', 'QQ': '110', 'email': 'zql@123.com'},
            # {'name': '吴小邪', 'tel': '111', 'QQ': '111', 'email': 'wx@123.com'},
            # {'name': '王月半', 'tel': '112', 'QQ': '112', 'email': 'wyb@123.com'}
        ]

    @staticmethod
    # 定义显示菜单功能函数
    def show_menu():
        """
        显示菜单
        :return:
        """
        print("")
        print("")
        print("*" * 50)
        print("欢迎使用【名片管理系统】v1.0")
        print("")
        print("1.新建名片")
        print("2.显示全部")
        print("3.查询名片")
        print("")
        print("0.退出系统")
        print("*" * 50)

    # 定义新建名片功能函数
    def new_card(self):
        """
        新建名片
        :return:
        """
        # 1.获取用户输入信息
        name = input("请输入姓名：")
        tel = input("请输入电话：")
        QQ = input("请输入QQ号：")
        email = input("请输入邮箱：")
        # 2.将获取的输入保存到字典中
        new_dict = {'name': name,
                    'tel': tel,
                    'QQ': QQ,
                    'email': email}
        # 3.将字典添加到列表
        self.card_list.append(new_dict)
        # 4.打印提示新建名片成功
        print("新建姓名是%s的名片成功" % name)

    # 定义显示全部名片功能函数
    def show_all_card(self):
        """
        显示全部名片
        :return:
        """
        # pass是占位符，起到完善语法结构的作用，不输出任何内容
        # pass
        # 0.判断表格是否有数据
        if len(self.card_list) == 0:
            print("当前名片列表无数据，请新建名片")
            # 代码不再向下执行
            return
        # 1.打印表头
        print("-" * 50)
        print("姓名".ljust(10), "电话".ljust(10), "QQ号".ljust(10), "邮箱".ljust(10))
        print("-" * 50)
        # 2.按照格式打印表格中的数据
        for i in self.card_list:
            # 临时变量i获取的是列表中的字典
            print(i.get('name').ljust(10), i.get('tel').ljust(10),
                  i.get('QQ').ljust(10), i.get('email').ljust(10))

    # 定义查询名片功能函数
    def search_card(self):
        """
        查询名片
        :return:
        """
        # 获取用户要查询的姓名
        find_name = input("请输入您要查询的姓名：")
        # 拿着要查询的姓名，到名片列表中查找
        for item in self.card_list:
            item.get('name')
            # 如果找到了，打印提示找到的信息
            if find_name == item.get('name'):
                print("已经找到姓名是%s的信息了" % find_name)
                print("-" * 50)
                print("姓名".ljust(10), "电话".ljust(10), "QQ号".ljust(10), "邮箱".ljust(10))
                print("-" * 50)
                print(item.get('name').ljust(10), item.get('tel').ljust(10),
                      item.get('QQ').ljust(10), item.get('email').ljust(10))
                print("-" * 50)
                self.deal_card(item)
                break
        else:
            print("您要查找的信息不存在！")

        # 如果没有找到，打印提示没有找到信息

    # 定义操作名片功能函数
    def deal_card(self, x):
        """
        操作名片：修改，删除，返回上一级
        :return:
        """
        # 获取用户的输入信息
        op = input("请输入对名片的操作选择[1.修改  2.删除  0.返回上一级]：")
        # 根据输入信息进行判断
        if op == '1':
            print("[功能]修改名片")
            x['name'] = self.input_card_info(x.get('name'), "请输入修改后的姓名[不修改直接回车]：")
            x['tel'] = self.input_card_info(x.get('tel'), "请输入修改后的电话[不修改直接回车]：")
            x['QQ'] = self.input_card_info(x.get('QQ'), "请输入修改后的QQ[不修改直接回车]：")
            x['email'] = self.input_card_info(x.get('email'), "请输入修改后的邮箱[不修改直接回车]：")
            print("修改名片成功！")
        elif op == '2':
            print("[功能]删除名片")
            self.card_list.remove(x)
            print("删除成功！")
        elif op == '0':
            print("[功能]返回上一级")
            return
        else:
            pass

    # input()函数扩充
    def input_card_info(self, value, msg):
        """
        实现input()函数扩充
        :return:
        """
        info = input(msg)
        if len(info) > 0:
            return info
        else:
            return value

    # 把名片列表保存到文件中
    def save_data(self):
        file = open("card_data.txt", "w", encoding="utf-8")
        file.write(str(self.card_list))
        file.close()

    # 当下次再启动名片管理系统时，要打开文件，读取文件内容到名片列表中
    def load_file(self):
        """
        实现当下次再启动名片管理系统时，要打开文件，读取文件内容到名片列表中
        :return:
        """
        if os.path.exists("card_data.txt"):
            print("文件存在，可以打开。")
            file = open("card_data.txt", "r", encoding="utf-8")
            text = file.read()
            print(text)
            print(type(text))
            if len(text) == 0:
                print("当前文件内容为空！")
                file.close()
                return
            # 把读取的文件内容 交给名片列表
            # 修改全局变量 添加global关键字 声明
            # global card_list
            self.card_list = eval(text)
        else:
            print("保存名片列表的文件不存在，请新建！")
