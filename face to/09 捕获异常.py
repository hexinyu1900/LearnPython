# 如果try部分出现了异常，except部分一定会执行
# 注意：只要捕获了异常，try部分无论有没有异常，程序都可以正常结束
try:
    int("123")
    print(num)
except:
    print("11111111111")

