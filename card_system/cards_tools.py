# 当前文件负责各个功能函数的实现和定义
# 实现的功能：显示菜单 新建名片 显示全部名片 查询名片 修改名片 删除名片

# 定义全局变量 名片列表
card_list = []
             # {'name': '张起灵', 'tel': '110', 'QQ': '110', 'email': 'zql@123.com'},
             # {'name': '吴小邪', 'tel': '111', 'QQ': '111', 'email': 'wx@123.com'},
             # {'name': '王月半', 'tel': '112', 'QQ': '112', 'email': 'wyb@123.com'}

# 定义显示菜单功能函数
def show_menu():
    '''
    显示菜单
    :return:
    '''
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
def new_card():
    '''
    新建名片
    :return:
    '''
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
    card_list.append(new_dict)
    # 4.打印提示新建名片成功
    print("新建姓名是%s的名片成功" % name)

# 定义显示全部名片功能函数
def show_all_card():
    '''
    显示全部名片
    :return:
    '''
    # pass是占位符，起到完善语法结构的作用，不输出任何内容
    # pass
    # 0.判断表格是否有数据
    if len(card_list) == 0:
        print("当前名片列表无数据，请新建名片")
        # 代码不再向下执行
        return
    # 1.打印表头
    print("-" * 50)
    print("姓名".ljust(10), "电话".ljust(10), "QQ号".ljust(10), "邮箱".ljust(10))
    print("-" * 50)
    # 2.按照格式打印表格中的数据
    for i in card_list:
        # 临时变量i获取的是列表中的字典
        print(i.get('name').ljust(10), i.get('tel').ljust(10),
              i.get('QQ').ljust(10), i.get('email').ljust(10))

# 定义查询名片功能函数
def search_card():
    '''
    查询名片
    :return:
    '''
    # 获取用户要查询的姓名
    find_name = input("请输入您要查询的姓名：")
    # 拿着要查询的姓名，到名片列表中查找
    for item in card_list:
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
            deal_card(item)
            break
    else:
        print("您要查找的信息不存在！")

    # 如果没有找到，打印提示没有找到信息

# 定义操作名片功能函数
def deal_card(x):
    '''
    操作名片：修改，删除，返回上一级
    :return:
    '''
    # 获取用户的输入信息
    op = input("请输入对名片的操作选择[1.修改  2.删除  0.返回上一级]：")
    # 根据输入信息进行判断
    if op == '1':
        print("[功能]修改名片")
        x['name'] = input_card_info(x.get('name'), "请输入修改后的姓名[不修改直接回车]：")
        x['tel'] = input_card_info(x.get('tel'), "请输入修改后的电话[不修改直接回车]：")
        x['QQ'] = input_card_info(x.get('QQ'), "请输入修改后的QQ[不修改直接回车]：")
        x['email'] = input_card_info(x.get('email'), "请输入修改后的邮箱[不修改直接回车]：")
        print("修改名片成功！")
    elif op == '2':
        print("[功能]删除名片")
        card_list.remove(x)
        print("删除成功！")
    elif op == '0':
        print("[功能]返回上一级")
        return
    else:
        pass

# input()函数扩充
def input_card_info(value, msg):
    '''
    实现input()函数扩充
    :return:
    '''
    info = input(msg)
    if len(info) > 0:
        return info
    else:
        return value
