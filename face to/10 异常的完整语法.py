try:
    # 可能会出现异常的代码
except 异常类型1:
    # 针对异常类型1的处理代码
except 异常类型2:
    # 针对异常类型2的处理代码
except (异常类型3,异常类型4):
    # 针对异常类型3或异常类型4的处理代码
except Exception as exp:
    # exp中获取异常的错误信息
    # except部分只有在发生异常时才会执行
else:
    # else部分在没有发生异常时才会执行
finally:
    # finally部分无论有没有异常都会执行