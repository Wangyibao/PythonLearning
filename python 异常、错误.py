try:
    r=10/0
    print('result',r)
except ZeroDivisionError as e:
    print('except',e)
else:
    print('没有错误则执行else')
finally:
    print('finally...')
print('end')

# 抛出错误
class FooError(ValueError):
    pass

def foo(s):
    n=int(s)
    if n==0:
        # 抛出异常
        raise FooError('invalid value: %s' %s)
    return 10/n

foo('0')

# 断言
def fee(s):
    n=int(s)
    assert n!=0,'n is zero!'
    return 10/n

def main():
    fee('0')

main()