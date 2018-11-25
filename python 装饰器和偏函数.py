# 装饰器
# 定义一个函数，打印时间字符串
def now():
    print('2018-11-11')

# 获取函数的名字
print(now.__name__)
print('----------------')
# 定义一个装饰器
def log(func):
    def wrapper(*args,**kw):
        print('call %s():' %func.__name__)
        return func(*args,**kw)
    return wrapper

# 给now函数加上装饰器
@log
def now():
    print('2018-11-11')

print(now())
print('--------------------------')
# 偏函数
import functools
# 偏函数：转换成二进制
int2=functools.partial(int,base=2)
print(int2('10000'))
# 调用函数，将参数更改
print(int2('10000',base=10))
