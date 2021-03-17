# def demo(num,*args,**kwargs):
#     print(num)
#     print(args)
#     print(kwargs)
#
# demo(10,4,15,"yuyuy",name="t昂二",age=10)
#
# def sum_numbers(*args):
#     sum=0
#     for i in args:
#         print(i)
#         sum+=i
#     return sum
#
# ret=sum_numbers(10,20)
# print(ret)

numbers = [1, 3, 6]
newNumbers = tuple(map(lambda x: x , numbers))
print(newNumbers)