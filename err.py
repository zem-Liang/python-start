try:
    n = int(input("输入一个数字："))
    result = 10 / n
    print(result)
except ValueError:
    print("这不是一个数字")
except ZeroDivisionError:
    print("不能除以0")