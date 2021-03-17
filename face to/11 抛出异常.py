def input_password():
    pwd = input("请输入密码：")
    # 如果用户密码长度<8,抛出异常
    if len(pwd) < 8:
        print("抛出异常")
        # ①使用Exception类创建对象
        ex = Exception("错误：密码长度小于8位")
        # ②使用raise抛出异常对象
        raise ex
    # 如果用户密码长度>=8,返回输入的密码
    else:
        return pwd

# input_password()

try:
    input_password()
except Exception as exp:
    print("捕获到异常：", exp)