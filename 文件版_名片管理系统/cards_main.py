# 总控中心
# 不需要实现各种功能，负责调度各种功能函数

import cards_tools

cards_tools.load_file()
# 添加死循环，让菜单重复显示
while True:
    # 显示菜单
    cards_tools.show_menu()
    # 获取用户输入选择
    op = input("请输入您的选择：")
    # print(op)
    # print(type(op))
    # 根据用户选择判断
    if op in ["1", "2", "3"]:
        print("用户选择与名片相关的操作.op：", op)
        #对op值进行进一步判断
        if op == "1":
            print("[功能]新建名片")
            cards_tools.new_card()
        elif op == "2":
            print("[功能]显示全部")
            cards_tools.show_all_card()
        else:
            print("[功能]查询名片")
            cards_tools.search_card()
    elif op == "0":
        # 当用户输入0想要退出名片管理系统，break跳出死循环
        cards_tools.save_data()
        print("退出系统")
        break
    else:
        print("您的输入有误，请重新输入。")


