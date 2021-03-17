# age=int(input("请输入年龄："))
# if age >= 18:
#     print("可以进入网吧")
#     print("欢迎来到异世界")
# else:
#     print("程序结束")
#
#
#
# age=int(input("请输入年龄："))
# if age>0 and age<=120:
#     print("输入正确")
# else:
#     print("输入错误")
#
# python_score=int(input("请输入python分数："))
# c_score=int(input("请输入c语言分数："))
# if python_score>60 or c_score>60:
#     print("成绩合格！")
# else:
#     print("成绩不合格！")

# is_employee=False
# if is_employee :
#     print("允许入内。")
# else:
#     print("不允许入内。")

# score = int(input("请输入分数："))
# if score < 60:
#     print("不及格")
# elif 60 <= score < 70:
#     print("差")
# elif 70 <= score < 80:
#     print("中")
# elif 80 <= score < 90:
#     print("良")
# elif score >= 90:
#     print("优")

has_ticket = False
if has_ticket:
    print("请进入安检！")
    knife_length = int(input("输入刀的长度："))
    if knife_length > 20:
        print("刀过长，不允许上车")
    else:
        print("安检通过")
else:
    print("不允许进入安检！")
