# import random
# random.randint(12, 20)  #生成的随机数n：  12<=n<=20
# random.randint(20, 20)  #结果永远是20
# random.randint(20, 10)  #该语句是错误的，下限必须小于上限


import random
print("石头=1,剪刀=2,布=3")
user_input = int(input("请输入玩家的数字："))
computer_input = random.randint(1, 3)
print("电脑的数字：", computer_input)

if user_input == computer_input:
    print("平手。")
elif (user_input == 1 and computer_input == 2) or (user_input == 2 and computer_input == 3) or (
        user_input == 3 and computer_input == 1):
    print("用户赢！")
else:
    print("电脑赢！")

